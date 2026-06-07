from sqlalchemy.orm import Session
from app.schemas.auth import RegisterRequest
from app.models.user import User
from app.auth.utils import hash_password

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