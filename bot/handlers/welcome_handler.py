from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram import Router


welcome_router = Router(name=__name__)


async def set_commands(bot):
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="about", description="О боте"),
        BotCommand(command="help", description="Показать помощь"),
    ]
    await bot.set_my_commands(commands)

@welcome_router.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(f'Salom {message.from_user.username}!')

@welcome_router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer('Developing')

@welcome_router.message(Command('about'))
async def command_about_handler(message: Message):
    await message.answer(f'{message.from_user.first_name} bu bot sizning IELTS Academic Writing Task 1 bilimizni tekshiradi')
