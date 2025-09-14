# app/auth.py
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone # <<< Still import timezone
from typing import Optional
from jose import JWTError, jwt


# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT Configuration
SECRET_KEY = "ETv5oQ3kwo3b2i9EgO-fKxhDBBYP36AJenJi6_takr4"  # <--- !!! CHANGE THIS TO A STRONG, RANDOM STRING !!!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token validity period

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=120)
    
    # --- IMPORTANT CHANGE HERE ---
    to_encode.update({"exp": expire}) # <<< Pass the datetime object directly, python-jose will convert to timestamp
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Gotta use this later for protected routes
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from . import models, schemas # Assuming your models and schemas are here

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # "token" will be our login endpoint path