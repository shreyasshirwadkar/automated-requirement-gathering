from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from database import Base
import uuid
from datetime import datetime

class DocumentVersion(Base):
    __tablename__ = "document_versions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id = Column(String, ForeignKey("documents.id"))
    version_number = Column(Integer, nullable=False)
    edited_by = Column(String, ForeignKey("users.id"))
    content = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    storage_location = Column(String)

    document = relationship("Document", back_populates="versions")
    editor = relationship("User")
    
    def __repr__(self):
        return f"<DocumentVersion {self.document_id} v{self.version_number}>"