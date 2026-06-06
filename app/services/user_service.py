from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def create_user(db: Session, data: UserCreate):
    try:
        new_user = User(
            username=data.username,
            email=data.email,
            password_hash=data.password,
            created_at=datetime.utcnow()
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    except IntegrityError:
        db.rollback()
        return None  # route handle http error


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, payload: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    if payload.username is not None:
        user.username = payload.username

    if payload.email is not None:
        user.email = payload.email

    if payload.password is not None:
        user.password_hash = payload.password

    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None
    
    db.delete(user)
    db.commit()

    return user