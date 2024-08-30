from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Schéma de base pour un lecteur
class ReaderBase(BaseModel):
    first_name: str
    last_name: str
    username: EmailStr

# Schéma pour créer un lecteur
class ReaderCreate(ReaderBase):
    password: str

# Schéma pour représenter un lecteur avec l'ID
class Reader(ReaderBase):
    id: int

    class Config:
        from_attributes = True  # Mise à jour pour Pydantic v2

# Schéma de base pour un livre
class BookBase(BaseModel):
    title: str
    author: str
    isbn: str

# Schéma pour créer un livre (sans ID, utilisé lors de la création)
class BookCreate(BookBase):
    pass

# Schéma pour représenter un livre avec l'ID
class Book(BookBase):
    id: int

    class Config:
        from_attributes = True  # Mise à jour pour Pydantic v2

# Schéma de base pour un emprunt
class BorrowBase(BaseModel):
    borrow_date: datetime
    return_date: Optional[datetime] = None

# Schéma pour créer un emprunt
class BorrowCreate(BorrowBase):
    reader_id: int
    book_id: int

# Schéma pour représenter un emprunt avec l'ID, le lecteur et le livre associés
class Borrow(BorrowBase):
    id: int
    reader: Reader
    book: Book

    class Config:
        from_attributes = True  # Mise à jour pour Pydantic v2
