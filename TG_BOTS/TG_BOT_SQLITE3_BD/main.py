import asyncio
from aiogram import Bot, Dispatcher, executor

from config import BOT_TOKEN

loop = asyncio.new_event_loop()
bot  = Bot(BOT_TOKEN, parse_mode='HTML')
dp   = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)

# Ссылки для SQL базы данных (в таблицу)
# URL_IPHONE13 = 'https://www.apple.com/shop/buy-iphone/iphone-13-pro'
# URL_MACBOOK  = 'https://www.apple.com/shop/buy-mac/macbook-pro/16-inch'
# URL_AIRPODS = 'https://www.apple.com/ru/airpods-pro/'

# URL_snakePlaylist = 'https://youtube.com/playlist?list=PLt-FKHWafkx4i_onIRN-kpgqhZ9XhTXq0'
# URL_platformerPlaylist = 'https://youtube.com/playlist?list=PLt-FKHWafkx71_KQcfsGJLtLu7O44J0Ws'
# URL_shooterPlaylist = 'https://youtube.com/playlist?list=PLt-FKHWafkx6Eg5v5BFNjS9c7iqlEXnsO'