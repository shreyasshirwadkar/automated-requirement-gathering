from sqlalchemy import Column, String, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.dbconfig.database import Base
import uuid
from datetime import datetime
from enum import Enum as PyEnum


class UserRole(PyEnum):
    analyst = "analyst"
    developer = "developer"
    admin = "admin"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True, autoincrement=False, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)  # Ensure this exists
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.analyst)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


    # projects = relationship("Project", back_populates="owner")

    def __repr__(self):
        return f"<User {self.name} ({self.email})>"
