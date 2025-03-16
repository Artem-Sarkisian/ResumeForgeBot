import asyncio
import logging
import os
from dotenv import load_dotenv
from app.handlers.base import router as base_router
from app.handlers.resume import router as resume_router
from app.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

load_dotenv()

async def main():
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Инициализация Redis из .env
    redis_url = f"redis://{os.getenv('REDIS_HOST', 'redis')}:{os.getenv('REDIS_PORT', '6379')}/1"
    redis_password = os.getenv('REDIS_PASSWORD', '')
    storage = RedisStorage.from_url(redis_url, password=redis_password)
    
    # Инициализация бота
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    dp = Dispatcher(storage=storage)
    
    # Подключение middlewares
    dp.message.middleware(LoggingMiddleware())
    
    # Регистрация роутеров
    dp.include_router(base_router)
    dp.include_router(resume_router)
    
    # Запуск бота
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())