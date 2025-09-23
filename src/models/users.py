from sqlalchemy import Integer, String, CheckConstraint, Enum
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from src.schemas.users import RelationshipStatus


class Base(DeclarativeBase):
    pass


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    surname: Mapped[str] = mapped_column(String(15))
    age: Mapped[int] = mapped_column(Integer, CheckConstraint("age < 100"))
    hobbies: Mapped[str | None] = mapped_column(String(100))
    relationship_status: Mapped[RelationshipStatus] = mapped_column(
        Enum(RelationshipStatus, values_callable=lambda x: [e.value for e in x])
    )

