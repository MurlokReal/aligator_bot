from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from keyboards.coaching_stuff_kb import get_coaching_stuff_kb, get_swimming_kb, get_diving_kb, get_water_polo_kb, get_aqua_aerobics_kb

router = Router()

image_main = FSInputFile("images/divider.png")
image_swimming = FSInputFile("images/coaching_stuff_menu/swimming.jpg")
image_water_polo = FSInputFile("images/coaching_stuff_menu/water_polo.jfif")
image_diving = FSInputFile("images/coaching_stuff_menu/diving.jpg")
image_aquaaerobics = FSInputFile("images/coaching_stuff_menu/aquaaerobics.jpeg")


@router.callback_query(F.data == "coaching_stuff")
async def coaching_stuff_handler(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media=image_main,
                                                            caption="<b>Выберите вид спорта:</b>"),
                                      reply_markup=get_coaching_stuff_kb())
    await callback.answer()


@router.callback_query(F.data == "swimming")
async def swimming_handler(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media=image_swimming,
                                                            caption="<b>Выберите тренера:</b>"),
                                     reply_markup=get_swimming_kb())
    await callback.answer()


@router.callback_query(F.data == "water_polo")
async def swimming_handler(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media=image_water_polo,
                                                            caption="<b>Выберите тренера:</b>"),
                                     reply_markup=get_water_polo_kb())
    await callback.answer()


@router.callback_query(F.data == "diving")
async def swimming_handler(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media=image_diving,
                                                            caption="<b>Выберите тренера:</b>"),
                                     reply_markup=get_diving_kb())
    await callback.answer()


@router.callback_query(F.data == "aquaaerobics")
async def swimming_handler(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media=image_aquaaerobics,
                                                            caption="<b>Выберите тренера:</b>"),
                                     reply_markup=get_aqua_aerobics_kb())
    await callback.answer()