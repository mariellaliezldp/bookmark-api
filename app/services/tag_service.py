from sqlalchemy.orm import Session

from app.schemas.tag import TagCreate, TagUpdate
from app.models.tag import Tag

def create_tag(db: Session, data: TagCreate):
    new_tag = Tag(
        name = data.name
    )

    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)

    return new_tag

def get_tags(db: Session):
    return db.query(Tag).all()

def get_tag(db: Session, tag_id: int):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()

    if not tag:
        return None
    
    return tag

def update_tag(db: Session, tag_id: int, data: TagUpdate):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()

    if not update_tag:
        return None
    
    if data.name is not None:
        tag.name = data.name

    db.commit()
    db.refresh(tag)

    return tag

def delete_tag(db: Session, tag_id: int):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()

    if not tag:
        return None
    
    return tag