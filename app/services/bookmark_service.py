from sqlalchemy.orm import Session

from app.models.bookmark import Bookmark
from app.models.tag import Tag
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate


def create_bookmark(db: Session, data: BookmarkCreate):
    new_bookmark = Bookmark(
        url=data.url,
        title=data.title,
        description=data.description,
        user_id=1
    )

    tag_objects = []

    for tag_name in data.tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()

        if not tag:
            tag = Tag(name=tag_name)
            db.add(tag)
            db.flush()

        tag_objects.append(tag)

    new_bookmark.tags = tag_objects

    db.add(new_bookmark)
    db.commit()
    db.refresh(new_bookmark)

    return new_bookmark


def get_bookmarks(db: Session):
    return db.query(Bookmark).all()


def get_bookmark(db: Session, bookmark_id: int):
    return db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()


def update_bookmark(db: Session, bookmark_id: int, data: BookmarkUpdate):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()

    if not bookmark:
        return None

    if data.url is not None:
        bookmark.url = data.url

    if data.title is not None:
        bookmark.title = data.title

    if data.description is not None:
        bookmark.description = data.description

    if data.tags is not None:
        tag_objects = []

        for tag_name in data.tags:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()

            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
                db.flush()

            tag_objects.append(tag)

        bookmark.tag = tag_objects

    db.commit()
    db.refresh(bookmark)

    return bookmark

def delete_bookmark(db: Session, bookmark_id: int):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()

    if not bookmark:
        return None
    
    db.delete(bookmark)
    db.commit()

    return bookmark