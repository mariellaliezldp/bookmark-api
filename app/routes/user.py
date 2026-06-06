from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import create_user, get_users, get_user, update_user, delete_user

router = APIRouter()

@router.post("/users")
def create_user_route(data: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, data)

    if not new_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    return new_user

@router.get("/users")
def get_users_route(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/users/{user_id}")
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.put("/users/{user_id}")
def update_user_route(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, payload)

    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user

@router.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    deletedUser = delete_user(db, user_id)

    if not deletedUser:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}