from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📑 Biz haqimizda'),
            KeyboardButton(text='📨 Murojaatlar'),
        ],
    ],
    resize_keyboard=True
)

biz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='💻 AKT haqida'),
            KeyboardButton(text='🛒 Magazinlar haqida'),
        ],

        [
            KeyboardButton(text='🏩 Davolanish'),
            KeyboardButton(text='🌿 Dehqonchilik'),
        ],

        [
            KeyboardButton(text='🐄 Chorvachilik'),
            KeyboardButton(text='🍇 Uzumchilik'),
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ],
    resize_keyboard=True
)


chek = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q"),
        ],
    ],
    resize_keyboard=True
)
