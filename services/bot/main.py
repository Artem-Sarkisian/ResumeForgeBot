import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот-помощник. Чем могу помочь?")
    
@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Список доступных команд:\n/start - начать диалог\n/help - список команд")
    
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())