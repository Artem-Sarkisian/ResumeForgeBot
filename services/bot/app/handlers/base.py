from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в Resume Forge Bot!\n\n"
        "Отправьте мне ваше резюме в формате PDF, DOCX или TXT, "
        "и я помогу сделать его лучше с помощью ИИ."
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "📋 <b>Resume Forge Bot</b> — улучшение резюме с помощью ИИ\n\n"
        "<b>Команды:</b>\n"
        "/start — Начать работу с ботом\n"
        "/help — Показать эту справку\n"
        "/status — Проверить статус подписки\n\n"
        "<b>Как использовать:</b>\n"
        "1. Отправьте резюме в формате PDF, DOCX или TXT\n"
        "2. Выберите направление для улучшения\n"
        "3. Получите улучшенную версию\n\n"
        "У вас есть одно бесплатное улучшение."
    )
    await message.answer(help_text, parse_mode="HTML")