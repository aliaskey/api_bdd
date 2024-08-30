# Lancer le serveur FastAPI avec Uvicorn
Ensuite, tu peux démarrer ton application FastAPI en utilisant Uvicorn, qui est un serveur ASGI léger pour FastAPI.

Commande pour lancer le serveur FastAPI :
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001


arret dans terminal uvicorn:
taskkill /F /PID 15884 sur un terminal
ctrl+C sur le terminal ou a ete run l'app

Cette commande force la fermeture (/F) du processus avec l'ID de processus (/PID) 23488.

Explication :
uvicorn app.main:app : Cela indique à Uvicorn de démarrer l'application FastAPI définie dans app.main.
--reload : Cette option est utile en développement car elle recharge automatiquement l'application chaque fois que tu modifies le code.