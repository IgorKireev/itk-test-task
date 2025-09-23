from enum import StrEnum
from pydantic import BaseModel, Field

class RelationshipStatus(StrEnum):
    SINGLE = "single"
    IN_RELATIONSHIP = "in relationship"
    MARRIED = "married"

class UserBase(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    surname: str = Field(min_length=2, max_length=15)
    age: int = Field(lt=100)
    hobbies: str
    relationship_status: RelationshipStatus


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=15)
    surname: str | None = Field(None, min_length=2, max_length=15)
    age: int | None = Field(None, lt=100)
    hobbies: str | None = None
    relationship_status: RelationshipStatus | None = None
