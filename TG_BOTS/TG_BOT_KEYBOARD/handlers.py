from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
# Для обработки команд и получения текста
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard, keyboard1, phone_key, mac_key, cb

from main import bot, dp
from config import chat_id

# Функция приветствия, отправка при старте
# Записываем их в диспетчер обновлений
async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')


# Section: ReplyKeyboardMarkup

# Обработка получения команды /shop
@dp.message_handler(Command('shop'))
async def show_shop(message: Message):
    # на получение команды /shop -> открываем клавиатуру
    await message.answer('shop', reply_markup=keyboard)

# Обработка нажатия кнопок
# Фильтрация получения только через текст в названиях кнопок
@dp.message_handler(Text(equals=['btn1', 'btn2', 'btn3']))
# Получаем продукты
async def get_goods(message: Message):
    # Убираем клавиатуру
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())


# Section: InlineKeyboardMarkup

# Обработка получения команды /tshop
@dp.message_handler(Command('tshop'))
async def show(message: Message):
    await message.answer(text='Buy or cancel', reply_markup=keyboard1)

# Обработка из keyboards.py по name(проверка имени товара)
@dp.callback_query_handler(text_contains='phone')
async def phone(call: CallbackQuery):
    # Даем 60 сек на попытку подключения к ссылке
    await call.answer(cache_time=60)
    # Если ссылка получила запрос, то открываем функцию
    await call.message.answer('Купить', reply_markup=phone_key)

@dp.callback_query_handler(text_contains='mac')
async def mac(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Купить', reply_markup=mac_key)
# OR ------------------------- с выводом полей с помощью словаря из keyboards.py
# 
# @dp.callback_query_handler(cb.filter(name='mac'))
# async def mac(call: CallbackQuery, callback_data: dict):
#     await call.answer(cache_time=60)

#     p = callback_data.get('price')

#     await call.message.answer(f'Купить. Он стоит: {p}', reply_markup=mac_key)

@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    # Выводим уведомление, что произошла отмена
    await call.answer('Отмена', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)    