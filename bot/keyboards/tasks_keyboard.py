from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Writing Task 1 Report Checker")], 
        [KeyboardButton(text="Writing Task 1 Letter Checker")],
        [KeyboardButton(text="Writing Task 2 Essay Checker")]
    ],
    resize_keyboard=True
)
