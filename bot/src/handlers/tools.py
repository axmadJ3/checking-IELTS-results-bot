from aiogram import F
from aiogram import Router
from aiogram.types import Message

from bot.src.keyboards import tasks_keyboard


tools_router = Router()


@tools_router.message(F.text == 'Writing Tasks')
async def writing_tasks_handler(message: Message):
    await message.answer(
        'Choose your writing task⬇', 
        reply_markup=tasks_keyboard.writing_keyboard
    )
