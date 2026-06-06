from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base
from app.models.bookmark_tags import bookmark_tags

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(200), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    tags = relationship(
        "Tag",
        secondary=bookmark_tags,
        back_populates="bookmarks"
    )