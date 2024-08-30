from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Borrow
from app.schemas import BorrowCreate, Borrow as BorrowSchema  # Importation du schéma Pydantic
from datetime import datetime
from typing import List
from app.schemas import BookCreate, Book as BookSchema


router = APIRouter(
    prefix="/borrows",
    tags=["Borrows"]
)

from sqlalchemy.orm import joinedload

@router.get("/", response_model=List[BorrowSchema])
def get_all_borrows(db: Session = Depends(get_db)):
    return db.query(Borrow).options(joinedload(Borrow.reader), joinedload(Borrow.book)).all()


# Création d'un emprunt
@router.post("/", response_model=BorrowSchema)
def create_borrow(request: BorrowCreate, db: Session = Depends(get_db)):
    print(request)  # Debugging
    new_borrow = Borrow(
        reader_id=request.reader_id,
        book_id=request.book_id,
        borrow_date=request.borrow_date
    )
    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)
    return new_borrow


# Récupération des emprunts par lecteur
@router.get("/reader/{reader_id}", response_model=List[BorrowSchema])  # Utilisation du schéma Pydantic ici
def get_borrow_by_reader(reader_id: int, db: Session = Depends(get_db)):
    return db.query(Borrow).filter(Borrow.reader_id == reader_id).all()

# Retourner un livre
@router.put("/return/{borrow_id}", response_model=BorrowSchema)  # Utilisation du schéma Pydantic ici
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).filter(Borrow.id == borrow_id).first()
    if not borrow:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Borrow with id {borrow_id} not found")
    borrow.return_date = datetime.utcnow()
    db.commit()
    return borrow

# Vérifier la disponibilité d'un livre
@router.get("/availability/{book_id}")
def is_book_available(book_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).filter(Borrow.book_id == book_id, Borrow.return_date == None).first()
    return {"available": borrow is None}
