from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterRequest
from app.database import get_db
from app.services.auth_service import register_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register_route(data: RegisterRequest, db: Session = Depends(get_db)):
    result = register_user(db, data)

    if result == "email_taken":
        raise HTTPException(status_code=400, detail="Email already exists")
    
    if result == "username_taken":
        raise HTTPException(status_code=400, detail="Username already exists")
    
    return result