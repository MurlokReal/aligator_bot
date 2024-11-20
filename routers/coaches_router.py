from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from keyboards.coaches_kb import get_coaches_basic_kb

router = Router()


@router.callback_query(F.data == "reshetilova")
async def reshetilova_handler(callback: CallbackQuery):
    image = FSInputFile("images/coaching_stuff/reshetilova.jfif")

    message_text = """Решетилова Арина Евгеньевна

КМС по плаванию, многократный чемпион Крыма и города Севастополя, призер Чемпионата Южного федерального округа, специалист в области физической культуры и спорта (СевГУ) 

Услуги:
- Оздоровительное плавание для детей и взрослых
- Спортивные плавание для детей

Свободные места (МГУ):
Пн, ср, пт 
18:00
Вт, чт
16:00

+79782876690
@locun"""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text,
                                        reply_markup=get_coaches_basic_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "sherstyuk")
async def sherstyuk_handler(callback: CallbackQuery):
    image = FSInputFile("images/coaching_stuff/sherstyuk.jfif")

    message_text = """Шерстюк Михаил Олегович

Мастер спорта, 
Закончил Университет Физической Культуры и спорта Украины в г. Киев
Обладатель Кубка Украины

Услуги:
-Водное поло для начинающих и продолжающих
- Плавание

Свободные места (Нахимовское училище):
Пн, ср, пт
9:30 - плавание

+7 978 967 7935
https://t.me/@id1831111167"""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text,
                                        reply_markup=get_coaches_basic_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "geevskiy")
async def geevskiy_handler(callback: CallbackQuery):
    image = FSInputFile("images/coaching_stuff/geevskiy.jpg")

    message_text = """Геевский Владимир Владимирович

Мастер спорта по водному поло.
Высшее образование по специальности: " Физическое воспитание" ТНУ ( КФУ) им. В.И. Вернадского

Услуги:
-Водное поло для начинающих и продолжающих
-Плавание

Свободные места (МГУ):
Пн, ср, пт
7:30, 18:00, 19:00
Вт, чт
16:00
Сб 
10:00

+7 (978) 857-33-62"""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text,
                                        reply_markup=get_coaches_basic_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "miskyiv")
async def miskyiv_handler(callback: CallbackQuery):
    image = FSInputFile("images/coaching_stuff/no_photo.webp")

    message_text = """Миськив Светлана Игоревна

МС по плаванию

Услуги:
-Спортивное плавание
-Оздоровительное плавание

+7 (978) 934-53-78
+7 (978) 943-03-05"""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text,
                                        reply_markup=get_coaches_basic_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "krasivskaya")
async def krasivskaya_handler(callback: CallbackQuery):
    image = FSInputFile("images/coaching_stuff/no_photo.webp")

    message_text = """Красивская Ирина Яковлевна

Услуги:
-Спортивное плавание
-Оздоровительное плавание

+7 (978) 826-52-50"""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text,
                                        reply_markup=get_coaches_basic_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "nasennikova")
async def nasennikova_handler(callback: CallbackQuery):
    image = FSInputFile("images/coaching_stuff/no_photo.webp")

    message_text = """Насенникова Маргарита Павловна 

Услуги:
-Аквааэробика

Свободные места (МГУ):
Пн, ср, пт
7:30
Вт, чт 
20:00

+7 (978) 857-33-62"""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text,
                                        reply_markup=get_coaches_basic_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "pechenina")
async def pechenina_handler(callback: CallbackQuery):
    image = FSInputFile("images/coaching_stuff/pechenina.jpg")

    message_text = """Печенина Инна Павловна

КМС по прыжкам в воду,
Многократный призер города Харькова и Украины, специалист в области культуры и спорта (КФУ им. Вернадского)

Обучаю прыжкам в воду на двухчасовых тренировках: 
В ЗАЛЕ - разминка, растяжка, ОФП, акробатика, прыжки на маты.
НА ВОДЕ - прыжки с вышек от 1 до 10 метров с элементами акробатики.
 Группы: 
1. Пн, Ср, Пт - 17:00
2. Вт, Чт - 18:00

+7 (978)018-44-73

Тренировки в спорткомплексе МГУ."""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text,
                                        reply_markup=get_coaches_basic_kb())
    await callback.message.delete()
    await callback.answer()