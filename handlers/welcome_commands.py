from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router


welcom_router = Router(name=__name__)


@welcom_router.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(f'Salom {message.from_user.username}!')

@welcom_router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer(f'{message.from_user.first_name} bu bot xali test jarayonida')

@welcom_router.message(Command('about'))
async def command_about_handler(message: Message):
    await message.answer(f'{message.from_user.first_name} bu bot xali test jarayonida')
