from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate, BookmarkResponse
from app.services.bookmark_service import create_bookmark, get_bookmarks, get_bookmark, update_bookmark, delete_bookmark, get_bookmark_stats
from app.models.user import User
from app.auth.deps import get_current_user

from datetime import datetime

router = APIRouter()

@router.post("/api/bookmarks")
def create_bookmark_route(
    data: BookmarkCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)):

    new_bookmark = create_bookmark(db, data, current_user.id)
    
    return new_bookmark

@router.get("/api/bookmarks")
def get_bookmarks_route(
    db: Session = Depends(get_db),
    q: str | None = None,
    tag: str | None = None,
    from_date: datetime | None = None,
    to_date: datetime | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    current_user: User = Depends(get_current_user)
):

    return get_bookmarks(
        db=db,
        user_id=current_user.id,
        q=q,
        tag=tag,
        from_date=from_date,
        to_date=to_date,
        page=page,
        limit=limit
    )

@router.get("/api/bookmarks/stats")
def get_bookmark_stats_route(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_bookmark_stats(db, current_user.id)

@router.get("/api/bookmarks/{bookmark_id}")
def get_bookmark_route(
    bookmark_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)):

    bookmark = get_bookmark(db, bookmark_id, current_user.id)

    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    return bookmark

@router.put("/api/bookmarks/{bookmark_id}")
def update_bookmark_route(bookmark_id: int, data: BookmarkUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated_bookmark = update_bookmark(db, bookmark_id, data, current_user.id)

    if not updated_bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    return updated_bookmark

@router.delete("/api/bookmarks/{bookmark_id}")
def delete_bookmark_route(bookmark_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted_bookmark = delete_bookmark(db, bookmark_id, current_user.id)

    if not deleted_bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    return {"message": "Bookmark deleted successfully"}
    
