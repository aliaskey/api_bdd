# Récapitulatif des commandes d'Alembic pour gérer les migrations de schéma de ta base de données :

Résumé des commandes terminal :
Activer l'environnement virtuel :
.\env\Scripts\activate  # Windows


Appliquer les migrations Alembic :
alembic upgrade head


Lancer le serveur FastAPI avec Uvicorn :
uvicorn app.main:app --reload

Accéder à l'application dans le navigateur :

Application : http://127.0.0.1:8000
Documentation Swagger : http://127.0.0.1:8000/docs

Documentation Redoc : http://127.0.0.1:8000/redoc


### 1. **Initialiser Alembic dans un projet**
   - **Commande :**
     ```bash
     alembic init alembic
     ```
   - **Description :**
     Crée la structure de répertoires nécessaire pour Alembic dans ton projet, y compris le répertoire `alembic/`, le fichier `alembic.ini`, et les fichiers de configuration par défaut.

### 2. **Créer une nouvelle révision (migration)**
   - **Commande avec autogénération :**
     ```bash
     alembic revision --autogenerate -m "Message de migration"
     ```
   - **Commande sans autogénération :**
     ```bash
     alembic revision -m "Message de migration"
     ```
   - **Description :**
     Crée un nouveau fichier de migration dans `alembic/versions/`. Avec `--autogenerate`, Alembic détecte automatiquement les changements dans les modèles SQLAlchemy et génère les migrations correspondantes. Sans `--autogenerate`, tu dois manuellement écrire les instructions de migration.

### 3. **Appliquer une migration à la base de données**
   - **Commande :**
     ```bash
     alembic upgrade head
     ```
   - **Description :**
     Applique toutes les migrations qui n'ont pas encore été appliquées jusqu'à la révision la plus récente (head). Tu peux aussi spécifier une révision particulière pour n'appliquer que certaines migrations.

### 4. **Rétrograder (annuler) une migration**
   - **Commande :**
     ```bash
     alembic downgrade -1
     ```
   - **Description :**
     Annule la dernière migration appliquée. Le `-1` indique que tu souhaites rétrograder d'une seule migration. Tu peux aussi spécifier un identifiant de révision spécifique pour rétrograder à un état particulier.

### 5. **Afficher l'historique des migrations**
   - **Commande :**
     ```bash
     alembic history
     ```
   - **Description :**
     Affiche l'historique complet des migrations appliquées et celles en attente. Utile pour voir l'ordre dans lequel les migrations ont été appliquées.

### 6. **Afficher l'état actuel des migrations (version de la base de données)**
   - **Commande :**
     ```bash
     alembic current
     ```
   - **Description :**
     Affiche la révision actuelle appliquée à la base de données, c'est-à-dire la dernière migration appliquée.

### 7. **Vérifier les différences entre le modèle et la base de données**
   - **Commande :**
     ```bash
     alembic check
     ```
   - **Description :**
     Compare les modèles SQLAlchemy avec le schéma actuel de la base de données pour détecter des divergences. Cette commande est utile pour s'assurer que tout est synchronisé.

### 8. **Exécuter une migration en mode hors ligne**
   - **Commande :**
     ```bash
     alembic upgrade head --sql
     ```
   - **Description :**
     Génère un script SQL pour la migration sans appliquer les changements directement à la base de données. Cela est utile pour examiner ou appliquer manuellement les changements.

### 9. **Appliquer une migration spécifique**
   - **Commande :**
     ```bash
     alembic upgrade <révision>
     ```
   - **Description :**
     Applique une migration spécifique identifiée par l'ID de révision.

### 10. **Rétrograder à une migration spécifique**
   - **Commande :**
     ```bash
     alembic downgrade <révision>
     ```
   - **Description :**
     Rétrograde la base de données à une révision spécifique, annulant toutes les migrations appliquées après cette révision.

### 11. **Réinitialiser la base de données en appliquant toutes les migrations**
   - **Commande :**
     ```bash
     alembic downgrade base
     alembic upgrade head
     ```
   - **Description :**
     Rétrograde la base de données à l'état initial (avant toute migration), puis réapplique toutes les migrations. Cela permet de tester les migrations depuis le début.

### 12. **Lister toutes les commandes disponibles**
   - **Commande :**
     ```bash
     alembic help
     ```
   - **Description :**
     Affiche une liste complète des commandes disponibles avec Alembic.

### Conclusion

Ce récapitulatif couvre les commandes principales que tu utiliseras régulièrement avec Alembic pour gérer les migrations de ta base de données. Elles te permettent de créer, appliquer, annuler, et inspecter les migrations, garantissant que ton schéma de base de données reste synchronisé avec ton code. Si tu as des questions supplémentaires ou si tu souhaites explorer des commandes spécifiques, n'hésite pas à demander !