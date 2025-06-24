from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram import Router


welcome_router = Router(name=__name__)


async def set_commands(bot):
    commands = [
        BotCommand(command="start", description="Launch the bot"),
        BotCommand(command="about", description="About the bot"),
        BotCommand(command="help", description="Help"),
    ]
    await bot.set_my_commands(commands)

@welcome_router.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(f'Hi {message.from_user.username}!')

@welcome_router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer('In development🛠')

@welcome_router.message(Command('about'))
async def command_about_handler(message: Message):
    await message.answer(f'{message.from_user.first_name}, you can use this bot to find out your IELTS level!😊')
