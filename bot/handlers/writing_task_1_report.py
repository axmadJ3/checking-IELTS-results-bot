from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.utils.states import WritingTask1State
from bot.utils.deepseek_chat import ai_generate


writing_task_1_router = Router(name=__name__)


@writing_task_1_router.message(F.text == 'Writing Task 1 Report Checker')
async def task1_checker(message: Message):
    await message.answer('Send a topic')

@writing_task_1_router.message(WritingTask1State.topic_state)
async def get_topic(message: Message):
    pass

@writing_task_1_router.message(WritingTask1State.wait)
async def stop_flood(message: Message):
    await message.answer('Wait, your request is being processed⏲')

@writing_task_1_router.message()
async def generate_response(message: Message, state: FSMContext):
    await state.set_state(WritingTask1State.wait)
    response = await ai_generate(message.text)
    await message.answer(response, parse_mode='Markdown')
    await state.clear()
