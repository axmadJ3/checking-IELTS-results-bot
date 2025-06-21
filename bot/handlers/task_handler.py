from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext

from bot.utils.states import Gen
from bot.utils.deepseek_chat import ai_generate

task_router = Router(name=__name__)


@task_router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer('Подождите ваш запрос обрабатывается')

@task_router.message()
async def gen_response(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response, parse_mode='Markdown')
    await state.clear()
