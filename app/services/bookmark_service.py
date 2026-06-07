from sqlalchemy.orm import Session

from app.models.bookmark import Bookmark
from app.models.tag import Tag
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate

from datetime import datetime
from sqlalchemy import or_
from sqlalchemy import text


def create_bookmark(db: Session, data: BookmarkCreate, user_id: int):
    new_bookmark = Bookmark(
        url=data.url,
        title=data.title,
        description=data.description,
        user_id=user_id
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


def get_bookmarks(
        db: Session, 
        user_id: int,
        q: str | None = None,
        tag: str | None = None,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
        page: int = 1,
        limit: int = 10):
    
    query = db.query(Bookmark).filter(Bookmark.user_id == user_id)

    # Seacrh title or description
    if q:
        query = query.filter(
            or_(
                Bookmark.title.ilike(f"%{q}%"),
                Bookmark.description.ilike(f"%{q}%")
            )
        )

    # Tag filter
    if tag:
        query = query.join(Bookmark.tags).filter(
            Tag.name.ilike(f"%{tag}%")
        )
        
   # Date filters
    if from_date:
        query = query.filter(
            Bookmark.created_at >= from_date
        )

    if to_date:
        query = query.filter(
            Bookmark.created_at <= to_date
        )

    total = query.count()

    skip = (page - 1) * limit

    bookmarks = query.offset(skip).limit(limit).all()

    return {
        "data": bookmarks,
        "total": total,
        "page": page,
        "limit": limit
    }

def get_bookmark_stats(db: Session, user_id: int):

    # Total bookmarks
    total_bookmarks = db.execute(text("""
        SELECT COUNT(*)
        FROM bookmarks
        WHERE user_id = :user_id
    """), {"user_id": user_id}).scalar()

    # Total tags
    total_tags = db.execute(text("""
        SELECT COUNT(DISTINCT t.id)
        FROM tags t
        JOIN bookmark_tags bt ON t.id = bt.tag_id
        JOIN bookmarks b ON b.id = bt.bookmark_id
        WHERE b.user_id = :user_id
    """), {"user_id": user_id}).scalar()

    # Tap tags
    top_tags = db.execute(text("""
        SELECT t.name, COUNT(*) as count
        FROM tags t
        JOIN bookmark_tags bt ON t.id = bt.tag_id
        JOIN bookmarks b ON b.id = bt.bookmark_id
        WHERE b.user_id = :user_id
        GROUP BY t.name
        ORDER BY count DESC
        LIMIT 5
    """), {"user_id": user_id}).fetchall()

    # Bookmarks per month
    bookmarks_per_month = db.execute(text("""
        SELECT DATE_FORMAT(created_at, '%Y-%m') AS month,
                COUNT(*) as count
        FROM bookmarks
        WHERE user_id = :user_id
        GROUP BY month
        ORDER BY month
    """), {"user_id": user_id}).fetchall()

    return {
        "total_bookmarks": total_bookmarks,
        "total_tags": total_tags,
        "top_tags": [dict(row._mapping) for row in top_tags],
        "bookmarks_per_month": [dict(row._mapping) for row in bookmarks_per_month]
    }


def get_bookmark(db: Session, bookmark_id: int, user_id: int):
    return db.query(Bookmark).filter(Bookmark.id == bookmark_id, Bookmark.user_id == user_id).first()


def update_bookmark(db: Session, bookmark_id: int, data: BookmarkUpdate, user_id: int):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id, Bookmark.user_id == user_id).first()

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

        bookmark.tags = tag_objects

    db.commit()
    db.refresh(bookmark)

    return bookmark

def delete_bookmark(db: Session, bookmark_id: int, user_id: int):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id, Bookmark.user_id == user_id).first()

    if not bookmark:
        return None
    
    db.delete(bookmark)
    db.commit()

    return bookmark