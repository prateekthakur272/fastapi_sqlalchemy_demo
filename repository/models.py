from database import Base
from sqlalchemy import String, Text, Column, Integer

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True,)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    
    def __repr__(self):
        return f'<Note {self.id}>'