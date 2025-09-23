from enum import StrEnum
from pydantic import BaseModel, Field

class RelationshipStatus(StrEnum):
    SINGLE = "single"
    IN_RELATIONSHIP = "in relationship"
    MARRIED = "married"

class User(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    surname: str = Field(min_length=2, max_length=15)
    age: int = Field(lt=100)
    hobbies: str | None
    relationship_status: RelationshipStatus

