from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterRequest, LoginRequest
from app.database import get_db
from app.services.auth_service import register_user, login_user

router = APIRouter(tags=["Auth"])

@router.post("/api/auth/register")
def register_route(data: RegisterRequest, db: Session = Depends(get_db)):
    result = register_user(db, data)

    if result == "email_taken":
        raise HTTPException(status_code=400, detail="Email already exists")
    
    if result == "username_taken":
        raise HTTPException(status_code=400, detail="Username already exists")
    
    return result

@router.post("/api/auth/login")
def login_route(data: LoginRequest, db: Session = Depends(get_db)):
    result = login_user(db, data)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return result