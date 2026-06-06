from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(max_length=80)
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = Field(max_length=80)
    email: Optional[EmailStr]
    password: Optional[str]


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True
