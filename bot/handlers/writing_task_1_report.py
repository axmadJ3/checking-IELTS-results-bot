import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot.utils.states import WritingTask1State
from bot.utils.deepseek_chat import ai_generate
from bot.keyboards.answer_keyboard import keyboard


logger = logging.getLogger()

writing_task_1_router = Router(name=__name__)


@writing_task_1_router.message(F.text == 'Writing Task 1 Report Checker')
async def task1_checker(message: Message, state: FSMContext):
    await state.set_state(WritingTask1State.topic_state)
    await message.answer('Send a topic')

@writing_task_1_router.message(WritingTask1State.topic_state)
async def get_topic(message: Message, state: FSMContext):
    topic = message.text
    await state.update_data(topic=topic)
    await state.set_state(WritingTask1State.topic_image_state)
    await message.answer('Great! Now send your topic image')

@writing_task_1_router.message(WritingTask1State.topic_image_state)
async def get_image(message: Message, state: FSMContext):
    if not message.photo:
        await message.answer("❗ Please send an image — this step is required.")
        return  # не продолжаем дальше

    photo = message.photo[-1]
    image_info = photo.file_id

    await state.update_data(topic_image=image_info)

    await state.set_state(WritingTask1State.report_state)
    await message.answer("Nice! Now send your written report.")


@writing_task_1_router.message(WritingTask1State.report_state)
async def get_report(message: Message, state: FSMContext):
    await state.update_data(report=message.text)
    await state.set_state(WritingTask1State.generate)
    await message.answer('OK, press Check Report for answer', reply_markup=keyboard)

@writing_task_1_router.message(WritingTask1State.generate, F.text == 'Check Report')
async def generate_response(message: Message, state: FSMContext):
    await state.set_state(WritingTask1State.wait)
    
    await message.answer("Analyzing your report... Please wait ⏳")
    data = await state.get_data()
    topic = data.get("topic", "")
    report = data.get("report", "")
    topic_image = data.get("topic_image", "None")
    
    # Составляем промпт
    prompt = f"""Проверь и оцени IELTS Writing Task 1.

Тема: {topic}
Изображение: {topic_image}
Отчёт:
{report}

Дай краткий комментарии по четырём критериям IELTS на английском:
- Task Achievement
- Coherence and Cohesion
- Lexical Resource
- Grammatical Range and Accuracy

Также укажи примерные баллы и советы по улучшению.
"""

    try:
        response = await ai_generate(prompt)
        await message.answer(response, parse_mode='Markdown', reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.error(f"Error while generating response: {e}")
        await message.answer("⚠️ Something went wrong. Please try again later.")
    finally:
        await state.clear()

@writing_task_1_router.message(WritingTask1State.wait)
async def stop_flood(message: Message):
    await message.answer('⏳ Please wait, your request is still being processed.')
