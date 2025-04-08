import torch
from transformers import AutoTokenizer, BertForSequenceClassification
import os

MODEL_DIR = os.path.dirname(__file__)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")

model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
model.to(device)
model.eval()

def check_spam(text: str) -> str:
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=512,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)

    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()
    return "Спам" if prediction == 1 else "Не спам"
