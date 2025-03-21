from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Общие настройки
    PROJECT_NAME: str = Field("resumeforgebot", description="Название проекта")
    ENVIRONMENT: str = Field("development", description="Окружение")
    
    # Настройки Telegram
    TELEGRAM_BOT_TOKEN: str = Field(..., description="Токен Telegram бота")
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "allow"
    }

# Глобальный экземпляр
try:
    settings = Settings()
except Exception as e:
    print(f"Ошибка конфигурации: {e}. Убедитесь, что указан TELEGRAM_BOT_TOKEN")
    settings = None