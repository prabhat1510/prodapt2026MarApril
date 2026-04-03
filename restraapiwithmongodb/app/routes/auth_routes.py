from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import User,Login,UserRegister
from app.services.auth_service import register_user, authenticate_user, generate_tokens
from app.utils.auth_dependency import get_current_user
from app.db.database import get_database
#from app.db.redis import redis_client

router = APIRouter()

@router.post("/register")
def register(user_reg: UserRegister, db=Depends(get_database)):
    user = User(username=user_reg.username, email=user_reg.email, password=user_reg.password, role="user")
    register_user(user, db)
    return {"msg": "User created"}

@router.post("/login")
def login(user: Login, db=Depends(get_database)):
    db_user = authenticate_user(user.username, user.password, db)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return generate_tokens(db_user)

#Refresh Token
@router.post("/refresh")
def refresh(user=Depends(get_current_user)):
    return generate_tokens(user)

#Logout → blacklist token
@router.post("/logout")
def logout(token=Depends(get_current_user)):
    #redis_client.set(token, "blacklisted", ex=3600)
    return {"msg": "Logged out"}

#Protected
@router.get("/secure")
def secure(user=Depends(get_current_user)):
    return {"user": user}