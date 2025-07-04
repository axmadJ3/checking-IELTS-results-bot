import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.logger_config import setup_logger
from bot.src.utils.config import settings
from bot.src.handlers.tools import tools_router
from bot.src.handlers.start import start_router, set_commands
from bot.src.handlers.writing_task_1_report import writing_task_1_router


bot = Bot(
    token=settings.BOT_TOKEN, 
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)


async def main():
    dp = Dispatcher()
    dp.include_routers(
        start_router, 
        writing_task_1_router,
        tools_router
    )
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    setup_logger(__name__)
    asyncio.run(main())
