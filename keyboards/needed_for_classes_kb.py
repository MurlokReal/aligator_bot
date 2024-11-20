from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_needed_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Обязательный инвентарь", callback_data="mandatory_inventory"))
    kb.add(InlineKeyboardButton(text="Медицинские справки", callback_data="medical_certificates"))
    kb.add(InlineKeyboardButton(text="Дополнительный инвентарь", callback_data="additional_inventory"))
    kb.add(InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    kb.adjust(1)
    return kb.as_markup()


def get_mandatory_inventory_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="🩱 Плавки/купальник 🩳", callback_data="swimsuit"),
           InlineKeyboardButton(text="🧢 Шапочка", callback_data="cap"),
           )
    kb.row(
        InlineKeyboardButton(text="🕶️ Очки", callback_data="glasses"),
        InlineKeyboardButton(text="🏖️ Полотенце", callback_data="towel"),
    )
    kb.row(
        InlineKeyboardButton(text="🩴 Тапочки", callback_data="slippers"),
        InlineKeyboardButton(text="🧼 Мыло и мочалка 🧽", callback_data="soap")
    )
    kb.row(InlineKeyboardButton(text="🔙 Назад", callback_data="needed_for_classes"),
        InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"),
    )
    return kb.as_markup()


def get_additional_inventory_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Ласты", callback_data="flippers"),
           InlineKeyboardButton(text="Лопатки", callback_data="paddles")
           )
    kb.row(InlineKeyboardButton(text="Трубка для плавания (сноркель)", callback_data="snorkel")
           )
    kb.row(InlineKeyboardButton(text="🔙 Назад", callback_data="needed_for_classes"),
           InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    return kb.as_markup()

def get_final_needed_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="🔙 Назад", callback_data="needed_for_classes"))
    kb.add(InlineKeyboardButton(text="📋 Главное меню", callback_data="main_menu"))
    kb.adjust(1)
    return kb.as_markup()