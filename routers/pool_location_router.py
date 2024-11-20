from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from keyboards.pool_location_kb import get_pool_location_kb

router = Router()


@router.callback_query(F.data == "pool_location")
async def pool_location_handler(callback: CallbackQuery):

    message_text = "<b>Местоположение бассейна</b> "\
                   "\n"\
                   "Адрес: ул. Героев Севастополя, д. 7, спорткомплекс при МГУ."\
                   "\n\n"\
                   "Остановка общественного транспорта «Памятник Матросу Кошке»"

    image = FSInputFile("images/location.jfif")

    await callback.message.edit_media(media=InputMediaPhoto(media=image,
                                                            caption=message_text),
                                      reply_markup=get_pool_location_kb())
    await callback.message.edit_text(
        "<b>Местоположение бассейна</b> "
        "\n"
        "Адрес: ул. Героев Севастополя, д. 7, спорткомплекс при МГУ."
        "\n\n"
        "Остановка общественного транспорта «Памятник Матросу Кошке»",
        reply_markup=get_pool_location_kb()
    )

    await callback.answer()

