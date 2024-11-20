import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import os
from dotenv import load_dotenv

from routers import main_menu_router, pool_location_router, coaching_stuff_router, needed_for_classes_router, coaches_router

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

TOKEN = os.getenv("TOKEN")


async def main():
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(
                  parse_mode=ParseMode.HTML
              ))
    dp = Dispatcher()

    dp.include_router(main_menu_router.router)
    dp.include_router(pool_location_router.router)
    dp.include_router(coaching_stuff_router.router)
    dp.include_router(needed_for_classes_router.router)
    dp.include_router(coaches_router.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
