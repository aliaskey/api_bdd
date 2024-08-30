from fastapi import FastAPI
from app.database import engine
from app import models
from app.auth.authentification import router as auth_router
from app.crud.db_user import router as user_router
from app.crud.db_book import router as book_router
from app.crud.db_borrow import router as borrow_router

# Crée l'application FastAPI
app = FastAPI()

# Crée les tables dans la base de données si elles n'existent pas
models.Base.metadata.create_all(bind=engine)

# Inclut les routes d'authentification, utilisateur, livre, et emprunt
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(book_router)
app.include_router(borrow_router)
