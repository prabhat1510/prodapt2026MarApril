from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from app.core.config import settings
from app.db.database import get_database

security = HTTPBearer()

def get_current_user(credentials=Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        print("Payload---",payload)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# RBAC #List of Roles
def require_role(roles: list[str]):
    def role_checker(user=Depends(get_current_user)):
        print("Roles ----",roles)
        print("User ----",user)
        #user.get("roles") is a list needs to check in roles which is another list
        if not any(role in roles for role in user.get("roles", [])):
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_checker