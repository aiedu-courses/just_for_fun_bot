from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    bot_token: str

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные
        # (относительно текущей рабочей директории)
        env_file = ".env"

        # Кодировка читаемого файла
        env_file_encoding = "utf-8"
