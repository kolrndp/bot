from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from spam_filter.spam_utils import check_spam

router = Router()

class SpamStates(StatesGroup):
    waiting_for_text = State()

@router.message(F.text.in_(["Проверить на спам", "/checkspam"]))
async def start_checking(message: Message, state: FSMContext):
    await message.answer("Пришлите сообщение, которое нужно проверить на спам")
    await state.set_state(SpamStates.waiting_for_text)

@router.message(SpamStates.waiting_for_text)
async def receive_text_for_spam_check(message: Message, state: FSMContext):
    text = message.text
    result = check_spam(text)
    await message.answer(f"Вы ввели: \"{text}\"\nРезультат: {result}")
    await state.clear()
