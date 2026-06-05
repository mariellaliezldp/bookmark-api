from pydantic import BaseModel, Field

class TagCreate(BaseModel):
    name: str = Field(max_length=50)

class TagResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True