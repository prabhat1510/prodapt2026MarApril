from app.core.security import hash_password, verify_password
from app.core.security import create_access_token, create_refresh_token
from app.utils.exceptions import UserExistsException,InvalidCredentialsException
from app.core.logger import setup_logger
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserDetails

logger = setup_logger()

def register_user(user, db):
    users = db.users
    if users.find_one({"username": user.username}):
        #add logging
        logger.error(f"User exists: {user.username}")
        raise UserExistsException("User exists")

    # Convert Pydantic model to dict for MongoDB
    user_data = user.model_dump()
    user_data["password"] = hash_password(user_data["password"])
    users.insert_one(user_data)

def authenticate_user(username, password, db):
    users = db.users
    user = users.find_one({"username": username})
    print("User ---authenticate---",user)
    if not user or not verify_password(password, user["password"]):
        logger.error(f"Invalid credentials for user: {username}")   
        raise InvalidCredentialsException("Invalid credentials")
    return user

def generate_tokens(user):
    if isinstance(user, dict):
        username = user.get("username") or user.get("sub")
        print("Username ---generate_tokens---",username)
        roles = user.get("roles")
        print("Role ---generate_tokens---",roles)
    else:
        username = getattr(user, "username", None) or getattr(user, "sub", None)
        roles = getattr(user, "roles", "user")
    
    payload = {"sub": username, "roles": roles}
    return {
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload)
    }

#Update User Details
def update_user(id: str, userDetails: UserDetails, db):
    return UserRepository(db).update_user(id, userDetails)

#Get User Details
def get_user_details(username: str, db):
    return UserRepository(db).get_user_by_username(username)