from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram import Router

from bot.src.keyboards import tasks_keyboard
from bot.src.utils import util_texts

start_router = Router(name=__name__)


async def set_commands(bot):
    commands = [
        BotCommand(command="start", description="Launch the bot"),
        BotCommand(command="about", description="About the bot"),
        BotCommand(command="help", description="Help"),
    ]
    await bot.set_my_commands(commands)

@start_router.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(
        util_texts.start_text(message.from_user.username),
        reply_markup=tasks_keyboard.keyboard
    )

@start_router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer('In development🛠')

@start_router.message(Command('about'))
async def command_about_handler(message: Message):
    await message.answer(util_texts.about_text(message.from_user.username))
