import logging
import os
import aiohttp
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from app.services.kafka import send_to_kafka

router = Router()

class ResumeStates(StatesGroup):
    waiting_for_resume = State()
    waiting_for_direction = State()
    processing = State()

@router.message(F.document)
async def process_document(message: Message, state: FSMContext):
    # Проверки документа и пользователя
    if not message.document or not message.from_user:
        await message.answer("Ошибка получения документа. Попробуйте снова.")
        return
        
    # Проверка имени файла
    if not message.document.file_name:
        await message.answer("Файл должен иметь название.")
        return
    
    # Проверка расширения
    file_ext = os.path.splitext(message.document.file_name)[1].lower()
    if file_ext not in ['.pdf', '.docx', '.txt']:
        await message.answer("Поддерживаются только форматы PDF, DOCX или TXT.")
        return
    
    # Сохраняем информацию
    file_info = {
        "file_id": message.document.file_id,
        "file_name": message.document.file_name,
        "mime_type": message.document.mime_type or "application/octet-stream",
        "user_id": message.from_user.id
    }
    
    await state.update_data(resume_file=file_info)
    
    # Создаем директорию
    os.makedirs("files", exist_ok=True)
    
    try:
        # Получаем файл
        file = await message.bot.get_file(message.document.file_id)
        
        # Формируем путь для сохранения
        destination = f"files/{message.from_user.id}_{message.document.file_id}{file_ext}"
        
        # Формируем URL для загрузки
        file_url = f"https://api.telegram.org/file/bot{message.bot.token}/{file.file_path}"
        
        # Загружаем файл
        async with aiohttp.ClientSession() as session:
            async with session.get(file_url) as resp:
                if resp.status == 200:
                    with open(destination, 'wb') as f:
                        f.write(await resp.read())
                else:
                    raise Exception(f"HTTP Error: {resp.status}")
        
        # Отправляем в Kafka
        await send_to_kafka("resume_upload", {
            "file_path": destination,
            "user_id": message.from_user.id,
            "file_name": message.document.file_name
        })
        
        await message.answer(
            "Ваше резюме получено! Начинаю обработку...\n"
            "Это может занять некоторое время."
        )
        
        # Устанавливаем состояние
        await state.set_state(ResumeStates.processing)
        
    except Exception as e:
        logging.error(f"Ошибка при загрузке файла: {e}")
        await message.answer("Произошла ошибка при обработке файла. Пожалуйста, попробуйте снова.")