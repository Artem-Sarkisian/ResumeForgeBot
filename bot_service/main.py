import asyncio
import logging
from aiogram import (Bot, Dispatcher)
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage

from app.config import settings
from app.handlers.base import router as base_router
from app.handlers.resume import router as resume_router
from app.middlewares.logging import LoggingMiddleware
from app.services.kafka import KafkaService

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
async def main():
    logger.info("Starting bot service")
    
    # Создаем Redis storage для FSM (Finite State Machine)
    storage = RedisStorage.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"
    )
    
    # Инициализируем бота и диспетчер
    bot = Bot(
        token=settings.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )
    dp = Dispatcher(storage=storage)
    
    # Регистрируем роутеры
    dp.include_router(base_router)
    dp.include_router(resume_router)
    
    # Регистрируем middleware
    dp.message.middleware(LoggingMiddleware())
    
    # Инициализация Kafka сервиса
    kafka_service = KafkaService(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        request_topic=settings.RESUME_REQUEST_TOPIC,
        response_topic=settings.RESUME_RESPONSE_TOPIC
    )
    
    # Запускаем сервис Kafka
    await kafka_service.start()
    
    # Добавляем Kafka в контекст бота для доступа из хэндлеров
    bot['kafka'] = kafka_service
    
    # Удаляем все предыдущие вебхуки и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    
    try:
        # Запуск бота в режиме long polling
        await dp.start_polling(bot)
    finally:
        # Корректное завершение сессии бота и остановка Kafka сервиса
        await bot.session.close()
        await kafka_service.stop()
        logger.info("Bot service stopped")

if __name__ == "__main__":
    # Запуск главной функции
    asyncio.run(main())