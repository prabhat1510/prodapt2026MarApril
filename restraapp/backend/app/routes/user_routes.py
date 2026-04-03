from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserDetails,Login,UserRegister,LoginResponse,Address
from app.services.user_service import register_user, authenticate_user, generate_tokens, update_user, get_user_details
from app.utils.auth_dependency import get_current_user, require_role
from app.db.database import get_database


router = APIRouter()

@router.post("/register")
def register(user_reg: UserRegister, db=Depends(get_database)):
    user = UserDetails(username=user_reg.username, email=user_reg.email, password=user_reg.password, roles=["user"], firstName="", lastName="", phone=user_reg.phone, homeAddress=Address(street="", city="", state="", zip=""))
    register_user(user, db)
    return {"msg": "User created"}

@router.post("/login",response_model=LoginResponse)
def login(user: Login, db=Depends(get_database)):
    db_user = authenticate_user(user.username, user.password, db)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    tokens=generate_tokens(db_user)
    return LoginResponse(roles=db_user["roles"],access_token=tokens["access_token"],refresh_token=tokens["refresh_token"],token_type="bearer")

#Refresh Token
@router.post("/refresh")
def refresh(user=Depends(get_current_user)):
    return generate_tokens(user)

#Logout → blacklist token
@router.post("/logout")
def logout(token=Depends(get_current_user)):
    #redis_client.set(token, "blacklisted", ex=3600)
    return {"msg": "Logged out"}


#Update user details
@router.put("/update/{id}")
def update_userdetails(id: str, userDetails: UserDetails, db=Depends(get_database), user=Depends(require_role(['admin','owner']))):
    return update_user(id, userDetails, db)

#Get User Details
@router.get("/details")
def get_user_profile(user=Depends(get_current_user), db=Depends(get_database)):
    return get_user_details(user["sub"], db)