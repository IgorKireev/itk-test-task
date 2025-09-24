"""Модуль для работы с crud операциями, связанными с пользователем."""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.users import UserCreate, UserUpdate
from src.models.users import UsersOrm
from src.exceptions.exceptions import bad_request


class UsersCRUD:
    """CRUD-операции для работы с пользователями."""

    @staticmethod
    async def get_users(session: AsyncSession) -> list[UsersOrm]:
        """
        Получить список всех пользователей, отсортированных по ID.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :return: Список пользователей.
        :rtype: list[UsersOrm]
        """

        query = select(UsersOrm).order_by(UsersOrm.id)
        result = await session.execute(query)
        users = result.scalars().all()
        return list(users)

    @staticmethod
    async def get_user(user_id: int, session: AsyncSession) -> UsersOrm | None:
        """
        Получить пользователя по ID.

        :param user_id: Идентификатор пользователя.
        :type user_id: int
        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :return: Объект пользователя или None, если не найден.
        :rtype: UsersOrm | None
        """

        return await session.get(UsersOrm, user_id)

    @staticmethod
    async def create_user(user_data: UserCreate, session: AsyncSession) -> UsersOrm:
        """
        Создать нового пользователя.

        :param user_data: Данные нового пользователя.
        :type user_data: UserCreate
        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :raises HTTPException: При ошибке добавления записи.
        :return: Созданный пользователь.
        :rtype: UsersOrm
        """

        user = UsersOrm(
            name=user_data.name,
            surname=user_data.surname,
            age=user_data.age,
            hobbies=user_data.hobbies,
            relationship_status=user_data.relationship_status,
        )
        try:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
        except IntegrityError:
            await session.rollback()
            raise bad_request()

    @staticmethod
    async def update_user(
        user_id: int, user_data: UserUpdate, session: AsyncSession
    ) -> UsersOrm | None:
        """
        Обновить данные пользователя.

        :param user_id: Идентификатор пользователя.
        :type user_id: int
        :param user_data: Обновлённые данные пользователя.
        :type user_data: UserUpdate
        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :raises HTTPException: При ошибке обновления.
        :return: Обновлённый пользователь или None, если пользователь не найден.
        :rtype: UsersOrm | None
        """

        user = await session.get(UsersOrm, user_id)
        if user is None:
            return None
        data = user_data.model_dump()
        data = {key: value for key, value in data.items() if value is not None}
        for key, value in data.items():
            setattr(user, key, value)
        try:
            await session.commit()
            await session.refresh(user)
            return user
        except IntegrityError:
            await session.rollback()
            raise bad_request()

    @staticmethod
    async def delete_user(user_id: int, session: AsyncSession) -> bool:
        """
        Удалить пользователя по ID.

        :param user_id: Идентификатор пользователя.
        :type user_id: int
        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :raises HTTPException: При ошибке удаления.
        :return: True, если пользователь удалён, иначе False.
        :rtype: bool
        """

        user = await session.get(UsersOrm, user_id)
        if user is None:
            return False
        try:
            await session.delete(user)
            await session.commit()
            return True
        except IntegrityError:
            await session.rollback()
            raise bad_request()
