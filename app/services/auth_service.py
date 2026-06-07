from sqlalchemy.orm import Session
from app.schemas.auth import RegisterRequest, LoginRequest
from app.models.user import User
from app.auth.utils import hash_password, verify_password, create_access_token

def register_user(db: Session, data: RegisterRequest):

    existing_email = db.query(User).filter(User.email == data.email).first()
    if existing_email:
        return "email_taken"
    
    existing_username = db.query(User).filter(User.username == data.username).first()
    if existing_username:
        return "username_taken"

    new_user = User(
        username = data.username,
        email = data.email,
        password_hash = hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db: Session, data: LoginRequest):

    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        return None
    if not verify_password(data.password, user.password_hash):
        return None
    
    token = create_access_token({
        "user_id": user.id,
        "email": user.email
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }