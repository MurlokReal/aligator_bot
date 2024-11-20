from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto

from keyboards.main_menu_kb import get_main_menu_kb

router = Router()

image = FSInputFile("images/main_menu.png")


@router.message(Command("start"))
async def cmd_start(message: Message):

    await message.answer_photo(photo=image,
                               caption="Вас приветствует чат-бот Аллигатор! Что вас интересует?",
                               reply_markup=get_main_menu_kb())



@router.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: CallbackQuery):

    await callback.message.answer_photo(photo=image,
                                        caption="Вы вернулись в главное меню! Что вас интересует?",
                                        reply_markup=get_main_menu_kb())
    await callback.message.delete()
    await callback.answer()
