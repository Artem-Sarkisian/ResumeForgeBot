import logging
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # Логируем входящие сообщения
        if isinstance(event, Message) and event.text:
            user_id = event.from_user.id if event.from_user else "Unknown"
            username = event.from_user.username or "No username"
            logging.info(f"Получено сообщение от {user_id} (@{username}): {event.text}")
        
        # Передаем управление дальше
        return await handler(event, data)