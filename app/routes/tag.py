from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.tag import TagCreate, TagUpdate
from app.services.tag_service import create_tag, get_tags, get_tag, update_tag, delete_tag

router = APIRouter()

@router.post("/tags")
def create_tag_route(data: TagCreate, db: Session = Depends(get_db)):
    new_tag = create_tag(db, data)

    return new_tag

@router.get("/tags")
def get_tags_router(db: Session = Depends(get_db)):
    return get_tags(db)

@router.get("/tags/{tag_id}")
def get_tag_route(tag_id: int, db: Session = Depends(get_db)):
    tag = get_tag(db, tag_id)

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    return tag

@router.put("/tags/{tag_id}")
def update_tag_route(tag_id: int, data: TagUpdate, db: Session = Depends(get_db)):
    updated_tag = update_tag(db, tag_id, data)

    if not updated_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    return updated_tag

@router.delete("/tags/{tag_id}")
def delete_tag_route(tag_id: int, db: Session = Depends(get_db)):
    deleted_tag = delete_tag(db, tag_id)

    if not deleted_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    return {"message": "Tag successfully deleted"}