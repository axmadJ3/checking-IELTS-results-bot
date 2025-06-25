from aiogram.fsm.state import State, StatesGroup


class WritingTask1State(StatesGroup):
    topic_state = State()
    topic_image_state = State()
    report_state = State()
    generate = State()
    wait = State()
