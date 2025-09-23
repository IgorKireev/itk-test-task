from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.users import UserCreate, UserUpdate
from src.models.users import UsersOrm
from src.exceptions.exceptions import bad_request



class UserCRUD:
    @staticmethod
    async def get_users(session: AsyncSession) -> list[UsersOrm]:
        query = select(UsersOrm).order_by(UsersOrm.id)
        result = await session.execute(query)
        users = result.scalars().all()
        return list(users)


    @staticmethod
    async def get_user(
            user_id: int,
            session: AsyncSession
    ) -> UsersOrm | None:
        return await session.get(UsersOrm, user_id)


    @staticmethod
    async def create_user(
            user_data: UserCreate,
            session: AsyncSession
    ) -> UsersOrm:
        user = UsersOrm(
            name=user_data.name,
            surname=user_data.surname,
            age=user_data.age,
            hobbies=user_data.hobbies,
            relationship_status=user_data.relationship_status
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
        user_id: int,
        user_data: UserUpdate,
        session: AsyncSession
    ) -> UsersOrm | None:
        user = await session.get(UsersOrm, user_id)
        if user is None:
            return None
        data = user_data.model_dump()
        data = {
            key: value for key, value in data.items() if value is not None
        }
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
    async def delete_user(
            user_id: int,
            session: AsyncSession
    ) -> bool:
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