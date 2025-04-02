from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.user import get_main_menu

router = Router()

@router.message(Command("start"))
async def command_start_handler(message: Message):
    user_id = message.from_user.id
    await message.answer(
        text="Добро пожаловать в бота! Выберите действие:",
        reply_markup=get_main_menu(user_id)
    )
