from fastapi import APIRouter, status, Depends, Response
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.users import UsersCRUD
from src.schemas.users import UserCreate, User, UserUpdate
from src.config.config import get_session
from src.exceptions.exceptions import not_found


router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/', response_model=list[User])
async def get_users(session: Annotated[AsyncSession, Depends(get_session)]):
    return await UsersCRUD.get_users(session=session)


@router.get('/{user_id}', response_model=User)
async def get_user(
        user_id: int,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    user = await UsersCRUD.get_user(user_id, session)
    if user:
        return user
    raise not_found(entity='User')


@router.post("/", response_model=User)
async def create_user(
        user_data: UserCreate,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    return await UsersCRUD.create_user(user_data, session)

@router.put('/{user_id}')
async def upadte_user(
        user_id: int,
        user_data: UserUpdate,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    user = await UsersCRUD.update_user(
        user_data=user_data,
        user_id=user_id,
        session=session
    )
    if user:
        return user
    raise not_found(entity='User')

@router.delete("/{user_id}")
async def delete_user(
        user_id: int,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    success = await UsersCRUD.delete_user(user_id=user_id, session=session)
    if success:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise not_found(entity="User")