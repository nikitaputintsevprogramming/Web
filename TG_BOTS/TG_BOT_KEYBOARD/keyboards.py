from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# Импорт ссылок на товары
from config import URL_MACBOOK, URL_IPHONE13

# простая клавиатура
keyboard = ReplyKeyboardMarkup(
    # Список из кнопок(каждый из списков будет отдельной строкой)
    keyboard=[
        [
            KeyboardButton(text='btn1'),
            KeyboardButton(text='btn2')         
        ],
        [
            KeyboardButton(text='btn3'),
        ]
    ],
    # Равномерное изменение по рамзеру экрана
    resize_keyboard=True
)

# содержит информацию о нашем товаре
cb = CallbackData('buy', 'id', 'name', 'price')

# Клавиатура №2
keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Iphone 13', callback_data='buy:0:phone:1000'),
            InlineKeyboardButton(text='MacBook', callback_data='buy:1:mac:999999')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)
 
# клавиатуры - кнопки с товарами 
phone_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Купить', url=URL_IPHONE13)
        ]
    ]
)

mac_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Купить', url=URL_MACBOOK)
        ]
    ]
)