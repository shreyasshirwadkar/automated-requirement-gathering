from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import uuid
from datetime import datetime

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    project_id = Column(String, ForeignKey("projects.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="documents")
    versions = relationship("DocumentVersion", back_populates="document")
    requirements = relationship("Requirement", back_populates="document")
    ai_artifacts = relationship("AIArtifact", back_populates="document")
    
    def __repr__(self):
        return f"<Document {self.title}>"