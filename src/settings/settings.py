"""Модуль содержит общие настройки приложения."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс конфигурации приложения, загружающий переменные из файла `.env`.

    Атрибуты:
       DB_HOST (str): Адрес хоста базы данных.
       DB_PORT (int): Порт для подключения к базе данных.
       DB_USER (str): Имя пользователя базы данных.
       DB_PASS (str): Пароль пользователя базы данных.
       DB_NAME (str): Название базы данных.

    Свойства:
       DATABASE_URL_asyncpg (str): Строка подключения к базе данных PostgreSQL
       с использованием драйвера asyncpg.
    """

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def database_url_asyncpg(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
