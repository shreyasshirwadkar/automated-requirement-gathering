from sqlalchemy import Column, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from database import Base
import uuid
from datetime import datetime

class AIArtifact(Base):
    __tablename__ = "ai_artifacts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id = Column(String, ForeignKey("documents.id"))
    type = Column(String)
    content = Column(JSON)
    generated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("Document", back_populates="ai_artifacts")
    author = relationship("User")
    
    def __repr__(self):
        return f"<AIArtifact {self.id} ({self.type})>"