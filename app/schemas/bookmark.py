from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime

class BookmarkCreate(BaseModel):
    url: HttpUrl
    title: str = Field(max_length=200)
    description: str | None = Field(default=None, max_length=500)

class BookmarkResponse(BaseModel):
    id: int
    url: str
    title: str
    description: str | None
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True