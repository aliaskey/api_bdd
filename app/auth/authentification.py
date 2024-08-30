# Contenu :

# Fournit une route pour gérer la connexion et générer un token JWT.

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app.database import get_db
from app.auth.hash import Hash
from app.auth.oauth2 import create_access_token

# L'importation de get_user_by_username est déplacée à l'intérieur de la fonction pour éviter une dépendance circulaire
# from app.crud.db_user import get_user_by_username

router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Import local pour éviter la dépendance circulaire
    from app.crud.db_user import get_user_by_username

    # Récupère l'utilisateur par son nom d'utilisateur (email)
    user = get_user_by_username(db, request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    # Vérifie si le mot de passe fourni correspond à celui stocké
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    # Crée un token d'accès JWT
    access_token = create_access_token(data={'sub': user.email})

    # Retourne le token d'accès et d'autres informations utilisateur
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.email
    }
