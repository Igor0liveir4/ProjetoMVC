# 1. Hash e verificação de senha com bcrypt
# 2. Geração de token JWT
# 3. Leitura e validação do token vindo do cokie

from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# CryptContext - configura o bcrypt como algoritmo de hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função de senha
def hash_password(password: str):
    return pwd_context.hash(password)

def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)

# Função do token - JWT
def criar_token(data: dict):
    payload = data.copy()

    # Define o tempo de expiração do token
    expira = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload

    # Criar o token JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decodificar_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
