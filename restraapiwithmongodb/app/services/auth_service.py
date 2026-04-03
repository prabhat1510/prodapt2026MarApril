from app.core.security import hash_password, verify_password
from app.core.security import create_access_token, create_refresh_token
from app.utils.exceptions import UserExistsException,InvalidCredentialsException
from app.core.logger import setup_logger

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
    if not user or not verify_password(password, user["password"]):
        logger.error(f"Invalid credentials for user: {username}")   
        raise InvalidCredentialsException("Invalid credentials")
    return user

def generate_tokens(user):
    if isinstance(user, dict):
        username = user.get("username") or user.get("sub")
        role = user.get("role")
    else:
        username = getattr(user, "username", None) or getattr(user, "sub", None)
        role = getattr(user, "role", "user")
    
    payload = {"sub": username, "role": role}
    return {
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload)
    }