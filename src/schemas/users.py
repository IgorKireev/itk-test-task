"""
Модуль содержит схемы данных для операций с пользователями в приложении.
Используется Pydantic для валидации и сериализации данных.
"""

from enum import StrEnum
from pydantic import BaseModel, Field


class RelationshipStatus(StrEnum):
    SINGLE = "single"
    IN_RELATIONSHIP = "in relationship"
    MARRIED = "married"


class UserBase(BaseModel):
    """
    Базовая схема пользователя.

    Атрибуты:
        name (str): Имя пользователя (длина от 2 до 15 символов).
        surname (str): Фамилия пользователя (длина от 2 до 15 символов).
        age (int): Возраст пользователя (должен быть меньше 100).
        hobbies (str): Хобби и увлечения пользователя.
        relationship_status (RelationshipStatus): Семейное положение.
    """

    name: str = Field(min_length=2, max_length=15)
    surname: str = Field(min_length=2, max_length=15)
    age: int = Field(lt=100)
    hobbies: str
    relationship_status: RelationshipStatus


class UserCreate(UserBase):
    """
    Схема для создания нового пользователя.

    Наследует все атрибуты от UserBase.
    """

    pass


class User(UserBase):
    """
    Схема для возврата информации о пользователе.

    Атрибуты:
        id (int): Уникальный идентификатор пользователя.
        name (str): Имя пользователя.
        surname (str): Фамилия пользователя.
        age (int): Возраст пользователя.
        hobbies (str): Хобби и увлечения пользователя.
        relationship_status (RelationshipStatus): Семейное положение.
    """

    id: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """
    Схема для обновления данных пользователя.

    Атрибуты (опциональные):
        name (str | None): Новое имя пользователя.
        surname (str | None): Новая фамилия пользователя.
        age (int | None): Новый возраст пользователя.
        hobbies (str | None): Новые хобби и увлечения.
        relationship_status (RelationshipStatus | None): Новое семейное положение.
    """

    name: str | None = Field(None, min_length=2, max_length=15)
    surname: str | None = Field(None, min_length=2, max_length=15)
    age: int | None = Field(None, lt=100)
    hobbies: str | None = None
    relationship_status: RelationshipStatus | None = None
