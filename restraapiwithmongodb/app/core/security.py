from datetime import datetime, timedelta
from jose import jwt
import bcrypt  # bcrypt version compatibility hack
import logging

# Monkeypatch bcrypt for passlib compatibility if needed
if not hasattr(bcrypt, "__about__"):
    bcrypt.__about__ = bcrypt

from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt_sha256", "bcrypt"], deprecated="auto")

# Password hashing
def hash_password(password: str):
    # Bcrypt has a 72-byte limit, and recent versions throw ValueError if exceeded
    return pwd_context.hash(password[:72])

def verify_password(plain, hashed):
    # If hashed is null or weird, passlib might fail, but let's be safe
    if not hashed:
        return False
    return pwd_context.verify(plain[:72], hashed)

# Token creation
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)