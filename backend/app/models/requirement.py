from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import uuid
from datetime import datetime

class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id = Column(String, ForeignKey("documents.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    type = Column(String)
    created_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("Document", back_populates="requirements")
    creator = relationship("User")
    
    def __repr__(self):
        return f"<Requirement {self.title}>"