from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

# Modèle SQLAlchemy pour les lecteurs
class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    
    borrowings = relationship("Borrow", back_populates="reader")


# Modèle SQLAlchemy pour les livres
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    isbn = Column(String, unique=True, index=True)
    
    borrowings = relationship("Borrow", back_populates="book")


# Modèle SQLAlchemy pour les emprunts
class Borrow(Base):
    __tablename__ = 'borrows'
    id = Column(Integer, primary_key=True, index=True)
    reader_id = Column(Integer, ForeignKey('readers.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    
    reader = relationship("Reader", back_populates="borrowings")
    book = relationship("Book", back_populates="borrowings")
