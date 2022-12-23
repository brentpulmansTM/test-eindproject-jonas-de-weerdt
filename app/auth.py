from passlib.context import CryptContext
from sqlalchemy.orm import Session

import crud

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def get_hash(name):
    return pwd_context.hash(name)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_caretaker_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
