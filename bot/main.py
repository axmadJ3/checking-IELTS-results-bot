import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from bot.logger_config import setup_logger
from bot.handlers.welcome_handler import welcome_router, set_commands
from bot.handlers.writing_task_1_report import writing_task_1_router

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main():
    dp = Dispatcher()
    dp.include_routers(welcome_router, writing_task_1_router)
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    setup_logger(__name__)
    asyncio.run(main())
