from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    role: Optional[str] = "analyst"
    password: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class TokenPayload(BaseModel):
    sub: str
    exp: int

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

    class Config:
        orm_mode = True

