"""Модуль содержит эндпоинты, связанные с пользователем."""

from fastapi import APIRouter, status, Depends, Response
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.users import UsersCRUD
from src.schemas.users import UserCreate, User, UserUpdate
from src.config.config import get_session
from src.exceptions.exceptions import not_found


router = APIRouter(prefix='/users', tags=['Users'])


@router.get(
    '/',
    response_model=list[User],
    status_code=status.HTTP_200_OK,
    summary="Получить всех пользователей",
    description="Возвращает список всех пользователей",
)
async def get_users(session: Annotated[AsyncSession, Depends(get_session)]):
    """
    Получить список всех пользователей.

    :param session: Асинхронная сессия SQLAlchemy.
    :type session: AsyncSession
    :return: Список пользователей.
    :rtype: list[User]
    """

    return await UsersCRUD.get_users(session=session)


@router.get(
    '/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Получить пользователя по ID",
    description="Возвращает информацию о конкретном пользователе",
)
async def get_user(
        user_id: int,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    """
    Получить пользователя по ID.

    :param user_id: Идентификатор пользователя.
    :type user_id: int
    :param session: Асинхронная сессия SQLAlchemy.
    :type session: AsyncSession
    :raises HTTPException: 404, если пользователь не найден.
    :return: Пользователь.
    :rtype: User
    """

    user = await UsersCRUD.get_user(user_id, session)
    if user:
        return user
    raise not_found(entity='User')


@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Создать нового пользователя",
    description="Создает нового пользователя",
)
async def create_user(
        user_data: UserCreate,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    """
    Создать нового пользователя.

    :param user_data: Данные нового пользователя.
    :type user_data: UserCreate
    :param session: Асинхронная сессия SQLAlchemy.
    :type session: AsyncSession
    :return: Созданный пользователь.
    :rtype: User
    """

    return await UsersCRUD.create_user(user_data, session)


@router.put(
    '/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Обновить данные пользователя",
    description="Обновляет данные существующего пользователя",
)
async def update_user(
        user_id: int,
        user_data: UserUpdate,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    """
    Обновить данные пользователя.

    :param user_data: Обновленные данные пользователя.
    :type user_data: UserUpdate
    :param user_id: Идентификатор пользователя.
    :type user_id: int
    :param session: Асинхронная сессия SQLAlchemy.
    :type session: AsyncSession
    :raises HTTPException: 404, если пользователь не найден.
    :return: Обновленный пользователь.
    :rtype: User
    """

    user = await UsersCRUD.update_user(
        user_data=user_data,
        user_id=user_id,
        session=session
    )
    if user:
        return user
    raise not_found(entity='User')


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить пользователя",
    description="Удаляет пользователя из системы",
)
async def delete_user(
        user_id: int,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    """
    Удалить пользователя по ID.

    :param user_id: Идентификатор пользователя.
    :type user_id: int
    :param session: Асинхронная сессия SQLAlchemy.
    :type session: AsyncSession
    :raises HTTPException: 404, если пользователь не найден.
    :return: Пустой ответ с HTTP статусом 204.
    :rtype: Response
    """

    success = await UsersCRUD.delete_user(user_id=user_id, session=session)
    if success:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise not_found(entity="User")