from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Местоположение бассейна", callback_data="pool_location"))
    kb.add(InlineKeyboardButton(text="Виды спорта и тренерский состав", callback_data="coaching_stuff"))
    kb.add(InlineKeyboardButton(text="Что необходимо для занятий", callback_data="needed_for_classes"))
    kb.adjust(1)
    return kb.as_markup()
