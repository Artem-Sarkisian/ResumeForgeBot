import os
import pathlib

def create_file(path):
    # Создаем все родительские директории
    parent_dir = os.path.dirname(path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    
    # Создаем пустой файл
    pathlib.Path(path).touch()

def create_project_structure():
    # Корневая директория проекта
    project_root = "resume-bot"
    
    # Список файлов и директорий для создания
    files_to_create = [
        # Конфигурационные файлы верхнего уровня
        f"{project_root}/docker-compose.yml",
        f"{project_root}/.env",
        f"{project_root}/.gitignore",
        
        # Сервис телеграм-бота
        f"{project_root}/bot_service/Dockerfile",
        f"{project_root}/bot_service/requirements.txt",
        f"{project_root}/bot_service/main.py",
        f"{project_root}/bot_service/app/__init__.py",
        f"{project_root}/bot_service/app/config.py",
        f"{project_root}/bot_service/app/handlers/__init__.py",
        f"{project_root}/bot_service/app/handlers/base.py",
        f"{project_root}/bot_service/app/handlers/resume.py",
        f"{project_root}/bot_service/app/middlewares/__init__.py",
        f"{project_root}/bot_service/app/middlewares/logging.py",
        f"{project_root}/bot_service/app/models/__init__.py",
        f"{project_root}/bot_service/app/models/user.py",
        f"{project_root}/bot_service/app/services/__init__.py",
        f"{project_root}/bot_service/app/services/kafka.py",
        f"{project_root}/bot_service/app/services/file.py",
        
        # Сервис обработки нейросетью
        f"{project_root}/ai_processor_service/Dockerfile",
        f"{project_root}/ai_processor_service/requirements.txt",
        f"{project_root}/ai_processor_service/main.py",
        f"{project_root}/ai_processor_service/app/__init__.py",
        f"{project_root}/ai_processor_service/app/config.py",
        f"{project_root}/ai_processor_service/app/models/__init__.py",
        f"{project_root}/ai_processor_service/app/models/resume.py",
        f"{project_root}/ai_processor_service/app/services/__init__.py",
        f"{project_root}/ai_processor_service/app/services/kafka.py",
        f"{project_root}/ai_processor_service/app/services/deepseek.py",
        f"{project_root}/ai_processor_service/app/services/file.py",
        
        # Сервис обратной связи
        f"{project_root}/callback_service/Dockerfile",
        f"{project_root}/callback_service/requirements.txt",
        f"{project_root}/callback_service/main.py",
        f"{project_root}/callback_service/app/__init__.py",
        f"{project_root}/callback_service/app/config.py",
        f"{project_root}/callback_service/app/models/__init__.py",
        f"{project_root}/callback_service/app/models/result.py",
        f"{project_root}/callback_service/app/services/__init__.py",
        f"{project_root}/callback_service/app/services/kafka.py",
        f"{project_root}/callback_service/app/services/telegram.py",
        f"{project_root}/callback_service/app/services/storage.py",
        
        # Сервис хранения данных
        f"{project_root}/storage_service/Dockerfile",
        f"{project_root}/storage_service/requirements.txt",
        f"{project_root}/storage_service/main.py",
        f"{project_root}/storage_service/migrations/001_initial.sql",
        f"{project_root}/storage_service/migrations/002_indexes.sql",
        f"{project_root}/storage_service/app/__init__.py",
        f"{project_root}/storage_service/app/config.py",
        f"{project_root}/storage_service/app/models/__init__.py",
        f"{project_root}/storage_service/app/models/resume.py",
        f"{project_root}/storage_service/app/models/user.py",
        f"{project_root}/storage_service/app/services/__init__.py",
        f"{project_root}/storage_service/app/services/postgres.py",
        f"{project_root}/storage_service/app/services/redis.py",
        f"{project_root}/storage_service/app/services/minio.py",
        
        # Тесты
        f"{project_root}/tests/__init__.py",
        f"{project_root}/tests/conftest.py",
        f"{project_root}/tests/test_bot.py",
        f"{project_root}/tests/test_ai_processor.py",
        f"{project_root}/tests/test_callback.py",
        f"{project_root}/tests/test_storage.py",
    ]
    
    # Создание файлов
    for file_path in files_to_create:
        create_file(file_path)
    
    print("Структура проекта успешно создана!")

if __name__ == "__main__":
    create_project_structure()