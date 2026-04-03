from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from app.core.config import settings
#from app.db.redis import redis_client
from app.db.database import get_database

security = HTTPBearer()

def get_current_user(credentials=Depends(security)):
    token = credentials.credentials

    # Check blacklist
    #if redis_client.get(token):
    #    raise HTTPException(status_code=401, detail="Token revoked")

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# RBAC
def require_role(role: str):
    def role_checker(user=Depends(get_current_user)):
        if user.get("role") != role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_checker