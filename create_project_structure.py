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
    # Используем текущую директорию вместо создания новой
    project_root = ""
    
    # Список файлов и директорий для создания
    files_to_create = [
        # Конфигурационные файлы верхнего уровня
        f"{project_root}docker-compose.yml",
        f"{project_root}.env",
        f"{project_root}.gitignore",
        
        # Сервис телеграм-бота
        f"{project_root}services/bot/Dockerfile",
        f"{project_root}services/bot/pyproject.toml",
        f"{project_root}services/bot/main.py",
        f"{project_root}services/bot/app/__init__.py",
        f"{project_root}services/bot/app/config.py",
        f"{project_root}services/bot/app/handlers/__init__.py",
        f"{project_root}services/bot/app/handlers/base.py",
        f"{project_root}services/bot/app/handlers/resume.py",
        f"{project_root}services/bot/app/middlewares/__init__.py",
        f"{project_root}services/bot/app/middlewares/logging.py",
        f"{project_root}services/bot/app/models/__init__.py",
        f"{project_root}services/bot/app/models/user.py",
        f"{project_root}services/bot/app/services/__init__.py",
        f"{project_root}services/bot/app/services/kafka.py",
        f"{project_root}services/bot/app/services/file.py",
        
        # Сервис обработки нейросетью
        f"{project_root}services/ai_processor/Dockerfile",
        f"{project_root}services/ai_processor/pyproject.toml",
        f"{project_root}services/ai_processor/main.py",
        f"{project_root}services/ai_processor/app/__init__.py",
        f"{project_root}services/ai_processor/app/config.py",
        f"{project_root}services/ai_processor/app/models/__init__.py",
        f"{project_root}services/ai_processor/app/models/resume.py",
        f"{project_root}services/ai_processor/app/services/__init__.py",
        f"{project_root}services/ai_processor/app/services/kafka.py",
        f"{project_root}services/ai_processor/app/services/ai.py",
        f"{project_root}services/ai_processor/app/services/file.py",
        
        # Сервис обратной связи
        f"{project_root}services/callback/Dockerfile",
        f"{project_root}services/callback/pyproject.toml",
        f"{project_root}services/callback/main.py",
        f"{project_root}services/callback/app/__init__.py",
        f"{project_root}services/callback/app/config.py",
        f"{project_root}services/callback/app/models/__init__.py",
        f"{project_root}services/callback/app/models/result.py",
        f"{project_root}services/callback/app/services/__init__.py",
        f"{project_root}services/callback/app/services/kafka.py",
        f"{project_root}services/callback/app/services/telegram.py",
        f"{project_root}services/callback/app/services/storage.py",
        
        # Сервис хранения данных
        f"{project_root}services/storage/Dockerfile",
        f"{project_root}services/storage/pyproject.toml",
        f"{project_root}services/storage/main.py",
        f"{project_root}services/storage/migrations/001_initial.sql",
        f"{project_root}services/storage/migrations/002_indexes.sql",
        f"{project_root}services/storage/app/__init__.py",
        f"{project_root}services/storage/app/config.py",
        f"{project_root}services/storage/app/models/__init__.py",
        f"{project_root}services/storage/app/models/resume.py",
        f"{project_root}services/storage/app/models/user.py",
        f"{project_root}services/storage/app/services/__init__.py",
        f"{project_root}services/storage/app/services/postgres.py",
        f"{project_root}services/storage/app/services/redis.py",
        f"{project_root}services/storage/app/services/minio.py",
        
        # Тесты
        f"{project_root}tests/__init__.py",
        f"{project_root}tests/conftest.py",
        f"{project_root}tests/test_bot.py",
        f"{project_root}tests/test_ai_processor.py",
        f"{project_root}tests/test_callback.py",
        f"{project_root}tests/test_storage.py",
    ]
    
    # Создание файлов
    for file_path in files_to_create:
        create_file(file_path)
    
    print("Структура проекта успешно создана в текущей директории!")

if __name__ == "__main__":
    create_project_structure()