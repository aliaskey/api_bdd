# Contenu :

# Fournit les fonctions pour hacher et vérifier les mots de passe.

import bcrypt

class Hash:
    # Hacher un mot de passe en utilisant bcrypt
    @staticmethod
    def hash_password(password: str) -> str:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
        return hashed_password.decode('utf-8')

    # Vérifier si le mot de passe fourni correspond au mot de passe stocké (haché)
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        password_byte_enc = plain_password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_bytes)
