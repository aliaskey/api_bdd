from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import Reader  # Le modèle SQLAlchemy Reader
from app.schemas import ReaderCreate, Reader as ReaderSchema  # Le schéma Pydantic
from app.auth.hash import Hash
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Création d'un lecteur
@router.post("/", response_model=ReaderSchema)  # Utilisation du schéma Pydantic ici
def create_user(request: ReaderCreate, db: Session = Depends(get_db)):
    new_user = Reader(
        first_name=request.first_name,
        last_name=request.last_name,
        username=request.email,
        password=Hash.hash_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Récupération de tous les lecteurs
@router.get("/", response_model=list[ReaderSchema])  # Utilisation du schéma Pydantic ici
def get_all_readers(db: Session = Depends(get_db)):
    return db.query(Reader).all()

# Récupération d'un lecteur par ID
@router.get("/{reader_id}", response_model=ReaderSchema)  # Utilisation du schéma Pydantic ici
def get_reader(reader_id: int, db: Session = Depends(get_db)):
    reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if not reader:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Reader with id {reader_id} not found")
    return reader

# Suppression d'un lecteur par ID
@router.delete("/{reader_id}")
def delete_reader(reader_id: int, db: Session = Depends(get_db)):
    reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if not reader:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Reader with id {reader_id} not found")
    db.delete(reader)
    db.commit()
    return {"detail": "Reader deleted"}

# Fonction pour récupérer un utilisateur par son nom d'utilisateur
def get_user_by_username(db: Session, username: str):
    user = db.query(Reader).filter(Reader.email == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return user
