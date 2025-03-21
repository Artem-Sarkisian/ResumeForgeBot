import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.config import settings
from handlers.base import base_router
from handlers.resume import resume_router
    
async def main():
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(base_router, resume_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
        print('Bot started')
    except KeyboardInterrupt:
        print('Bot stopped')