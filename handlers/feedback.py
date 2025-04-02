from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class FeedbackStates(StatesGroup):
    waiting_for_theme = State()

@router.message(F.text.lower() == "указать название темы")
async def feedback_command_handler(message: Message, state: FSMContext):
    await message.answer("Введите тему:")
    await state.set_state(FeedbackStates.waiting_for_theme)

@router.message(FeedbackStates.waiting_for_theme)
async def process_theme(message: Message, state: FSMContext):
    theme = message.text
    await message.answer(f'Вы ввели тему: "{theme}"')
    await state.clear()