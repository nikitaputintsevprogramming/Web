import asyncio
from aiogram import Bot, Dispatcher, executor


from config import bot_token

loop = asyncio.new_event_loop()
# Создаем экземпляр нашего бота
bot = Bot(bot_token, parse_mode='HTML')
# Диспатчер отслеживает все обновления в нашем боте
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_hello
    # Запуск бота
    executor.start_polling(dp, on_startup=send_hello)