from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.bookmark_tags import bookmark_tags

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    bookmarks = relationship(
        "Bookmark",
        secondary=bookmark_tags,
        back_populates="tags"
    )