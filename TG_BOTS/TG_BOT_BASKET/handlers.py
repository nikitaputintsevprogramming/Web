from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType

from config import payments_token
from main import dp, bot
from shop import keyboard, cb

import sqlite3

# при команде /start
# передаем команду старт
@dp.message_handler(Command('start'))
# функция будет принимать на вход сообщение
async def start(message: Message):
    # при запуске сразу в БД будет сохранятся user_id пользователя и его name имя
    connect = sqlite3.connect('TG_BOT_BASKET.db')
    cursor = connect.cursor()
    # вместо вопросов - [1, 2] аргументы
    cursor.execute("""INSERT INTO users (user_id, name) VALUES (?,?)""", [message.chat.id, message.chat.first_name])
    cursor.close()
    connect.commit()
    connect.close()

    # приветствуем пользователя
    await message.answer("Hello")

# собираем корзину
# при команде /cart
@dp.message_handler(Command('cart'))
async def cart(message: Message):
    # для выбора товаров, какие хотим купить?
    await message.answer('Что хотите купить?', reply_markup=keyboard)

# обработчик 1-ой кнопки
# фильтр если id = 1(смартфон)
@dp.callback_query_handler(cb.filter(id='1'))
# по нажатию на кнопку - добавляем товар в корзину
async def smart(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=10)

    # добавляем запись в таблицу cart(корзина)
    # id товара
    product_id = callback_data.get('id')
    # id пользователя
    user_id = call.message.chat.id

    connect = sqlite3.connect('TG_BOT_BASKET.db')
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO cart (user_id, product_id) VALUES (?, ?)""", [user_id, product_id])
    cursor.close()
    connect.commit()
    connect.close()

    await call.message.answer('Added!')

# обработчик 2-ой кнопки
@dp.callback_query_handler(cb.filter(id='2'))
async def lap(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=10)

    product_id = callback_data.get('id')
    user_id = call.message.chat.id

    connect = sqlite3.connect('TG_BOT_BASKET.db')
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO cart (user_id, product_id) VALUES (?, ?)""", [user_id, product_id])
    cursor.close()
    connect.commit()
    connect.close()

    await call.message.answer('Added!')

# функция покупки
@dp.message_handler(Command('buy'))
async def buy(message: Message):
    connect = sqlite3.connect('TG_BOT_BASKET.db')
    cursor = connect.cursor()
    # достаем все из корзины с id покупателя
    data = cursor.execute("""SELECT * FROM cart WHERE user_id=(?)""", [message.chat.id]).fetchall()
    cursor.close()
    connect.commit()
    cursor = connect.cursor()
    print(data)
    new_data = []
    # создаем записи из корзины по товарам с id покупателя (id и name)
    for i in range(len(data)):
        new_data.append(cursor.execute("""SELECT * FROM products WHERE id=(?)""", [data[i][1]]).fetchall())
    cursor.close()
    connect.commit()
    connect.close()
    # генератор форматирования списка
    new_data = [new_data[i][0] for i in range(len(new_data))]
    # список из того, что покупаем (собираем цены)
    prices = [LabeledPrice(label=i[1], amount=i[2]) for i in new_data]

    await bot.send_invoice(message.chat.id,
                           title='Cart',
                           description='Description',
                           provider_token=payments_token,
                           currency='rub',
                           need_email=True,
                           prices=prices,
                           start_parameter='example',
                           payload='some_invoice')

# 
@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# функция о том, что платеж прошел успешно и очищаем корзину
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def s_pay(message: Message):
    connect = sqlite3.connect('TG_BOT_BASKET.db')
    cursor = connect.cursor()
    # очищаем корзину
    cursor.execute("""DELETE FROM cart WHERE user_id=(?)""", [message.chat.id])
    cursor.close()
    connect.commit()
    connect.close()
    await bot.send_message(message.chat.id, 'Платеж прошел успешно!!!')    