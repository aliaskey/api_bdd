Installation des dépendances avec pip

FastAPI : Framework principal pour créer l'API.
Uvicorn : Serveur ASGI pour exécuter l'application FastAPI.
SQLAlchemy : ORM pour interagir avec la base de données.
Alembic : Gestionnaire de migrations de schéma de base de données pour SQLAlchemy.
Pydantic : Utilisé par FastAPI pour la validation des données (inclus avec FastAPI).
bcrypt : Pour le hachage des mots de passe.
PyJWT : Pour gérer les tokens JWT pour l'authentification.

pip install fastapi uvicorn sqlalchemy alembic bcrypt PyJWT
pip freeze > requirements.txt
pip install -r requirements.txt


alembic==1.7.5
bcrypt==3.2.0
fastapi==0.75.0
PyJWT==2.3.0
SQLAlchemy==1.4.25
uvicorn==0.16.0

Utilisation d'Alembic
Alembic pour gérer les migrations de ta base de données, voici quelques commandes utiles :

Initialiser Alembic :
alembic init alembic

Cela crée un répertoire alembic/ et un fichier alembic.ini.

Créer une migration :
alembic revision --autogenerate -m "Initial migration"

Cette commande génère une nouvelle migration en fonction des modèles SQLAlchemy.

Appliquer les migrations :
alembic upgrade head

Conclusion
Environnement virtuel : Utiliser un environnement virtuel (venv) est essentiel pour maintenir les dépendances de ton projet isolées.
Installation des dépendances : pip install fastapi uvicorn sqlalchemy alembic bcrypt PyJWT.
Fichier requirements.txt : Il est crucial pour partager les dépendances de ton projet avec d'autres et pour faciliter le déploiement.
En suivant ces étapes, tu pourras configurer correctement ton environnement de développement pour créer et maintenir une API FastAPI bien structurée et facile à gérer.
