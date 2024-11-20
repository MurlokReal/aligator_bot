from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_coaches_basic_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="🔙 Назад", callback_data="coaching_stuff"))
    kb.add(InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    kb.adjust(1)
    return kb.as_markup()