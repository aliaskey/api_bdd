from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Book
from app.schemas import BookCreate, Book as BookSchema  # Importation du schéma Pydantic

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

# Création d'un livre
@router.post("/", response_model=BookSchema)  # Utilisation du schéma Pydantic ici
def create_book(request: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=request.title,
        author=request.author,
        isbn=request.isbn
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Récupération de tous les livres
@router.get("/", response_model=list[BookSchema])  # Utilisation du schéma Pydantic ici
def get_all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# Récupération d'un livre par ID
@router.get("/{book_id}", response_model=BookSchema)  # Utilisation du schéma Pydantic ici
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {book_id} not found")
    return book

# Suppression d'un livre par ID
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {book_id} not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted"}
