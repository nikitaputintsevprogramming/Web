from aiogram.types import Message

from main import bot, dp
from config import chat_id

# Функция приветствия, отправка при старте
# Записываем их в диспетчер обновлений
async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')

# Эхо сообщений
# Декоратор
# Диспетчер является обработчиком сообщений
@dp.message_handler()
async def send_answer(message: Message):
    text = message.text # or -> f'You are wrote: {message.text}'
    await message.answer(text=text)