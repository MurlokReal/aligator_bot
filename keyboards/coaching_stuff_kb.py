from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_coaching_stuff_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(
        InlineKeyboardButton(text="🏊 Плавание", callback_data="swimming"),
        InlineKeyboardButton(text="🤽 Водное поло", callback_data="water_polo"),
    )
    kb.row(
        InlineKeyboardButton(text="🤸 Прыжки в воду", callback_data="diving"),
        InlineKeyboardButton(text="🚶‍♀️ Аквааэробика", callback_data="aquaaerobics"),
    )
    kb.row(
        InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"),
    )
    return kb.as_markup()


def get_swimming_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Миськив Светлана Игоревна", callback_data="miskyiv"))
    kb.add(InlineKeyboardButton(text="Решетилова Арина Евгеньевна", callback_data="reshetilova"))
    kb.add(InlineKeyboardButton(text="Геевский Владимир Владимирович", callback_data="geevskiy"))
    kb.add(InlineKeyboardButton(text="Красивская Ирина Яковлевна", callback_data="krasivskaya"))
    kb.add(InlineKeyboardButton(text="🔙 Назад", callback_data="coaching_stuff"))
    kb.add(InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    kb.adjust(1)
    return kb.as_markup()


def get_water_polo_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Геевский Владимир Владимирович", callback_data="geevskiy"))
    kb.add(InlineKeyboardButton(text="Шерстюк Михаил Олегович", callback_data="sherstyuk"))
    kb.add(InlineKeyboardButton(text="🔙 Назад", callback_data="coaching_stuff"))
    kb.add(InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    kb.adjust(1)
    return kb.as_markup()


def get_diving_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Печенина Инна Павловна", callback_data="pechenina"))
    kb.add(InlineKeyboardButton(text="🔙 Назад", callback_data="coaching_stuff"))
    kb.add(InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    kb.adjust(1)
    return kb.as_markup()


def get_aqua_aerobics_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Насенникова Маргарита Павловна", callback_data="nasennikova"))
    kb.add(InlineKeyboardButton(text="🔙 Назад", callback_data="coaching_stuff"))
    kb.add(InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    kb.adjust(1)
    return kb.as_markup()