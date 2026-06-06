from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate, BookmarkResponse
from app.services.bookmark_service import create_bookmark, get_bookmarks, get_bookmark, update_bookmark, delete_bookmark

router = APIRouter()

@router.post("/bookmarks")
def create_bookmark_route(data: BookmarkCreate, db: Session = Depends(get_db)):
    new_bookmark = create_bookmark(db, data)
    
    return new_bookmark

@router.get("/bookmarks", response_model=list[BookmarkResponse])
def get_bookmarks_route(db: Session = Depends(get_db)):
    return get_bookmarks(db)

@router.get("/bookmarks/{bookmark_id}")
def get_bookmark_route(bookmark_id: int, db: Session = Depends(get_db)):
    bookmark = get_bookmark(db, bookmark_id)

    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    return bookmark

@router.put("/bookmarks/{bookmark_id}")
def update_bookmark_route(bookmark_id: int, data: BookmarkUpdate, db: Session = Depends(get_db)):
    updated_bookmark = update_bookmark(db, bookmark_id, data)

    if not updated_bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    return updated_bookmark

@router.delete("/bookmarks/{bookmark_id}")
def delete_bookmark_route(bookmark_id: int, db: Session = Depends(get_db)):
    deleted_bookmark = delete_bookmark(db, bookmark_id)

    if not deleted_bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    return {"message": "Bookmark deleted successfully"}
    
