from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def get_main_menu(user_id: int):

    main_menu_builder = ReplyKeyboardBuilder()
    main_menu_builder.add(KeyboardButton(text="Указать название темы"))

    return main_menu_builder.as_markup(resize_keyboard=True)