from sqlalchemy.orm import Session
from database.models.user import User
from database.models.post import Post
from database.config import SessionLocal

def get_users():
    with SessionLocal() as db:
        return db.query(User).all()

def create_user(email: str, name: str):
    with SessionLocal() as db:
        user = User(email=email, name=name)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user