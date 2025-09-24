"""Модуль содержит модель SQLAlchemy для работы с пользователями."""

from sqlalchemy import Integer, String, CheckConstraint, Enum
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from src.schemas.users import RelationshipStatus


class Base(DeclarativeBase):
    """Базовый класс для всех моделей данных."""

    pass


class UsersOrm(Base):
    """
     Модель для пользователя.

    Атрибуты:
        id: Первичный ключ (autoincrement)
        name: Имя пользователя.
        surname: Фамилия пользователя.
        age: Возраст пользователя.
        hobbies: Хобби пользователя.
        relationship_status: Семейное положение пользователя.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    surname: Mapped[str] = mapped_column(String(15))
    age: Mapped[int] = mapped_column(Integer, CheckConstraint("age < 100"))
    hobbies: Mapped[str] = mapped_column(String(100))
    relationship_status: Mapped[RelationshipStatus] = mapped_column(
        Enum(RelationshipStatus, values_callable=lambda x: [e.value for e in x])
    )

