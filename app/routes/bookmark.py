from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate, BookmarkResponse
from app.services.bookmark_service import create_bookmark, get_bookmarks, get_bookmark, update_bookmark, delete_bookmark
from app.models.user import User
from app.auth.deps import get_current_user

router = APIRouter()

@router.post("/api/bookmarks")
def create_bookmark_route(data: BookmarkCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_bookmark = create_bookmark(db, data, current_user.id)
    
    return new_bookmark

@router.get("/api/bookmarks", response_model=list[BookmarkResponse])
def get_bookmarks_route(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_bookmarks(db, current_user.id)

@router.get("/api/bookmarks/{bookmark_id}")
def get_bookmark_route(bookmark_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
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
    
