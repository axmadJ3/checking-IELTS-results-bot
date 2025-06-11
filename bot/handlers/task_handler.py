import asyncio

from aiogram.types import Message
from aiogram import Router

from bot.services.parser import run_parser


task_router = Router(name=__name__)

@task_router.message(lambda msg: msg.text == 'task')
async def run_task1_parser(message: Message):
    status = await asyncio.to_thread(run_parser, 'https://engnovate.com/ielts-academic-writing-task-1-report-checker/')
    await message.answer(f'Status code = {status}')
