from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards.needed_for_classes_kb import get_mandatory_inventory_kb, get_final_needed_kb, get_main_needed_kb, get_additional_inventory_kb

router = Router()

@router.callback_query(F.data == "needed_for_classes")
async def needed_for_classes_handler(callback: CallbackQuery):
    image_main = FSInputFile("images/inventory/inventory.jpeg")

    await callback.message.answer_photo(photo=image_main,
                                        caption="<b>Что необходимо для занятий:</b>",
                                        reply_markup=get_main_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "medical_certificates")
async def needed_for_classes_handler(callback: CallbackQuery):
    message_text = """Для получения справок вам нужно обратиться к педиатру/терапевту. У врача вы берете направление на анализ на энтеробиоз. После получение отрицательного анализа вы вновь посещаете педиатра/терапевта с результатом анализов и просите выписать справку со следующими фразами: «группа здоровья», «Д-учет» (при наличии), «допущен к занятиям в бассейне». Справки вы передаете тренеру."""

    await callback.message.answer(text=message_text,
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "mandatory_inventory")
async def needed_for_classes_handler(callback: CallbackQuery):

    image_main = FSInputFile("images/inventory/inventory.jpeg")

    await callback.message.answer_photo(photo=image_main,
                                        caption="<b>Обязательный инвентарь:</b>",
                                        reply_markup=get_mandatory_inventory_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "additional_inventory")
async def needed_for_classes_handler(callback: CallbackQuery):

    image_main = FSInputFile("images/inventory/inventory.jpeg")

    await callback.message.answer_photo(photo=image_main,
                                        caption="<b>Дополнительный инвентарь:</b>",
                                        reply_markup=get_additional_inventory_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "swimsuit")
async def swimsuit_handler(callback: CallbackQuery):
    image_swimsuit_1 = FSInputFile("images/inventory/swimsuit1.jfif")
    image_swimsuit_2 = FSInputFile("images/inventory/swimsuit2.jfif")
    image_swimsuit_3 = FSInputFile("images/inventory/swimsuit3.jfif")


    message_text = """Для занятий в бассейне мужчинам стоит отдать предпочтение плавкам классической модели или «боксерам» для плавания. Рекомендуем не брать плавательные шорты, т.к. во время плавания будет создаваться эффект «парашюта», который значительно замедлит вас в воде.

Для занятий в бассейне женщинам стоит отдать предпочтение слитным купальникам спортивных моделей. Они плотно прилегают к телу и имеют дополнительную подкладку, которая не просвечивает. Для обладательниц большого бюста рекомендуем купальники с широкими бретелями, которые не будут натирать плечи во время активных движений."""

    album_builder = MediaGroupBuilder(
        caption=message_text
    )
    album_builder.add(
        type="photo",
        media=image_swimsuit_1
    )
    album_builder.add(
        type="photo",
        media=image_swimsuit_2
    )
    album_builder.add(
        type="photo",
        media=image_swimsuit_3
    )

    await callback.message.answer_media_group(media=album_builder.build())
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "cap")
async def cap_handler(callback: CallbackQuery):
    image_cap_1 = FSInputFile("images/inventory/cap1.jfif")
    image_cap_2 = FSInputFile("images/inventory/cap2.jfif")
    image_cap_3 = FSInputFile("images/inventory/cap3.jfif")


    message_text = """В бассейне шапочка обязательна и женщинам, и мужчинам. Резиновые шапочки отлично сидят на голове даже при наличии длинных волос. Тряпичные шапочки, к сожалению, не подходят для занятий из-за неплотного прилегания к голове, который может создать дискомфорт во время заплыва. 

Детям до 5 лет рекомендуем брать детские шапочки. 

Обладателям дредов и объемных кос рекомендуем специальные шапочки. Они больше стандартных.
"""

    album_builder = MediaGroupBuilder(
        caption=message_text
    )
    album_builder.add(
        type="photo",
        media=image_cap_1
    )
    album_builder.add(
        type="photo",
        media=image_cap_2
    )
    album_builder.add(
        type="photo",
        media=image_cap_3
    )

    await callback.message.answer_media_group(media=album_builder.build())
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "glasses")
async def glasses_handler(callback: CallbackQuery):
    image_glasses_1 = FSInputFile("images/inventory/glasses1.jfif")
    image_glasses_2 = FSInputFile("images/inventory/glasses2.jfif")
    image_glasses_3 = FSInputFile("images/inventory/glasses3.jfif")


    message_text = """Перед приобретением очков для плавания обязательна примерка! Очки должны плотно прилегать к глазницам, а линзы очков – быть обтекаемыми. Если в комплекте с очками нет сменных переносиц, обратите внимание на длину «родной» переносицы. В области носа очки не должны пропускать воздух.

Не рекомендуем покупать маски и полу-маски.
"""

    album_builder = MediaGroupBuilder(
        caption=message_text
    )
    album_builder.add(
        type="photo",
        media=image_glasses_1
    )
    album_builder.add(
        type="photo",
        media=image_glasses_2
    )
    album_builder.add(
        type="photo",
        media=image_glasses_3
    )

    await callback.message.answer_media_group(media=album_builder.build())
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "towel")
async def towel_handler(callback: CallbackQuery):
    image_towel_1 = FSInputFile("images/inventory/towel1.jfif")
    image_towel_2 = FSInputFile("images/inventory/towel2.jfif")


    message_text = """Для занятий в бассейне вам подойдет любое полотенце. Если вы цените свободное место в вашем рюкзаке, рекомендуем полотенца из микрофибры. Среднее полотенце из этого материала по размеру сравнимо с бутылкой для воды, объемом 0,33 л. Также этот материал отлично впитывает воду и быстро сохнет.
"""

    album_builder = MediaGroupBuilder(
        caption=message_text
    )
    album_builder.add(
        type="photo",
        media=image_towel_1
    )
    album_builder.add(
        type="photo",
        media=image_towel_2
    )

    await callback.message.answer_media_group(media=album_builder.build())
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "slippers")
async def slippers_handler(callback: CallbackQuery):
    image_slippers_1 = FSInputFile("images/inventory/slippers1.jfif")
    image_slippers_2 = FSInputFile("images/inventory/slippers2.jfif")
    image_slippers_3 = FSInputFile("images/inventory/slippers3.jfif")
    image_slippers_4 = FSInputFile("images/inventory/slippers3.jfif")


    message_text = """Рекомендуем приобретать резиновые тапочки моделей «шлепки», «сабо» или «вьетнамки». Важно обратить внимание на протектор подошвы. Он должен быть не плоским, чтобы избежать падений в бассейне. 

Детям отлично подойдут резиновые сандали на липучке.
"""

    album_builder = MediaGroupBuilder(
        caption=message_text
    )
    album_builder.add(
        type="photo",
        media=image_slippers_1
    )
    album_builder.add(
        type="photo",
        media=image_slippers_2
    )
    album_builder.add(
        type="photo",
        media=image_slippers_3
    )
    album_builder.add(
        type="photo",
        media=image_slippers_4
    )

    await callback.message.answer_media_group(media=album_builder.build())
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "soap")
async def soap_handler(callback: CallbackQuery):
    image = FSInputFile("images/inventory/soap1.webp")
    message_text = """В общественном душе запрещено использовать различные гели и маски для волос. Они создают пленку на кафеле, на которой можно поскользнуться и упасть. Отлично подойдет обычное кусковое мыло и мочалка на ваше усмотрение."""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text)
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "flippers")
async def flippers_handler(callback: CallbackQuery):
    image = FSInputFile("images/inventory/flippers.jpg")
    message_text = """Ласты помогают не только плыть быстрее, но и улучшить положение тела в воде, увеличить силу ног и гибкость суставов. Для плавания в бассейне лучше выбрать короткие ласты. На ноге они должны сидеть плотно и обуваться с небольшим усилием."""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text)
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "paddles")
async def paddles_handler(callback: CallbackQuery):
    image = FSInputFile("images/inventory/paddles.jpg")
    message_text = """Лопатки предназначаются для увеличения скорости и силы гребка, заодно помогая довести до совершенства технику плавания. Лопатки должны быть немного длиннее ладони пловца и регулироваться затяжками."""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text)
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == "snorkel")
async def snorkel_handler(callback: CallbackQuery):
    image = FSInputFile("images/inventory/snorkel.jpg")
    message_text = """Во время тренировки пловец, используя сноркель, не отвлекается на повороты или подъем головы для выполнения вдоха. Это позволяет ему максимально сконцентрироваться на технике выполнения гребка и её проработке. Чем больше практики, тем быстрее пловец развивает технически правильный и сбалансированный гребок. Причем это важно не только для спринтеров. Многие пловцы на средние и длинные дистанции тренируются со сноркелем, чтобы развивать и закреплять длину гребка. Сноркель должен быть выбран в соответствии с размерной таблицей, которая включает в себя рост спортсмена. Обязательно наличие резинового загубника, с помощью которого спортсмен держит сноркель во рту."""

    await callback.message.answer_photo(photo=image,
                                        caption=message_text)
    await callback.message.answer(text="Меню",
                                  reply_markup=get_final_needed_kb())
    await callback.message.delete()
    await callback.answer()