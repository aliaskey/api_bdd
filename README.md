# Library API

Cette API permet de gérer une bibliothèque simple en utilisant FastAPI et SQLAlchemy. Elle permet de gérer des lecteurs, des livres, et des emprunts.

## Fonctionnalités

- Créer, lire, mettre à jour et supprimer des lecteurs (CRUD)
- Créer, lire, mettre à jour et supprimer des livres (CRUD)
- Gérer les emprunts de livres par les lecteurs
- Vérifier la disponibilité des livres
- Authentification des utilisateurs avec JWT

## Installation

1. Clonez le repository
2. Installez les dépendances avec `pip install -r requirements.txt`
3. Démarrez l'application avec `uvicorn app.main:app --reload`

## Utilisation

### Endpoints principaux

- **POST /readers/** : Créer un lecteur
- **GET /readers/** : Obtenir tous les lecteurs
- **POST /books/** : Créer un livre
- **GET /books/** : Obtenir tous les livres
- **POST /borrow/** : Emprunter un livre (requiert authentification)
- **POST /return/{borrow_id}** : Retourner un livre (requiert authentification)
- **GET /books/{book_id}/availability** : Vérifier la disponibilité d'un livre

### Authentification

- **POST /token** : Obtenir un token JWT

### Dépendances

- **FastAPI** : Framework pour construire l'API
- **SQLAlchemy** : ORM pour interagir avec la base de données
- **bcrypt** : Pour hacher les mots de passe
- **JWT** : Pour gérer l'authentification par token
