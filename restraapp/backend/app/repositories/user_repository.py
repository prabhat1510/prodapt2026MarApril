from app.schemas.user_schema import UserDetails,Login,UserRegister,LoginResponse,Address
from bson import ObjectId
from bson.errors import InvalidId
from pymongo.database import Database
from app.core.logger import setup_logger
from app.utils.exceptions import UserExistsException,InvalidCredentialsException,UserNotFoundException

logger = setup_logger()

class UserRepository: 
    def __init__(self, db: Database):
        self.db = db
        self.users = db.users

    def _format_document(self, doc):
        if doc and "_id" in doc:
            doc["id"] = str(doc.pop("_id"))
        return doc

    def create_user(self, user: UserDetails):
        result = self.users.insert_one(user.model_dump())
        return str(result.inserted_id)

    def get_user(self, id: str):
        try:
            doc = self.users.find_one({"_id": ObjectId(id)})
            return self._format_document(doc)
        except InvalidId:
            return None

    def get_user_by_username(self, username: str):
        doc = self.users.find_one({"username": username})
        return self._format_document(doc)

    def get_all_users(self):
        return [self._format_document(doc) for doc in self.users.find()]

    def update_user(self, id: str, user: UserDetails):
        try:
            self.users.update_one({"_id": ObjectId(id)}, {"$set": user.model_dump()})
            doc = self.users.find_one({"_id": ObjectId(id)})
            return self._format_document(doc)
        except InvalidId:
            return None

    def add_restaurant_to_user(self, user_id: str, restaurant_id: str):
        try:
            self.users.update_one(
                {"_id": ObjectId(user_id)},
                {"$addToSet": {"restaurant_ids": restaurant_id}}
            )
        except InvalidId:
            logger.error(f"Invalid user ID for adding restaurant: {user_id}")
            pass

    def delete_user(self, id: str):
        try:
            self.users.delete_one({"_id": ObjectId(id)})
        except InvalidId:
            pass