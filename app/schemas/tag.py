from pydantic import BaseModel, Field
from typing import Optional

class TagCreate(BaseModel):
    name: str = Field(max_length=50)

class TagUpdate(BaseModel):
    name: Optional[str]

class TagResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True