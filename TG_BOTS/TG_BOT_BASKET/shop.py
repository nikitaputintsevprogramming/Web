from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('buy', 'id')
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Smartphone: 10900p', callback_data='buy:1'),
            InlineKeyboardButton('Laptop: 189000p', callback_data='buy:2')
        ]        
    ]
)