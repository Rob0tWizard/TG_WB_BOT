from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Получить информацию по товару"),

        ],
        {
            KeyboardButton(text="Остановить уведомления"),

        },
        [
            KeyboardButton(text="Получить информацию из БД"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)

del_kb = ReplyKeyboardRemove()
