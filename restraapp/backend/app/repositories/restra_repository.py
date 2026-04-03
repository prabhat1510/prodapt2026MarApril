from app.schemas.restra_schema import Restraunt, UpdateRestraunt, RestrauntResponse
from bson import ObjectId
from bson.errors import InvalidId
from pymongo.database import Database
from app.core.logger import setup_logger
from app.utils.exceptions import RestrauntNotFoundException

logger = setup_logger()

class RestrauntRepository:  
    def __init__(self, db: Database):
        self.db = db
        self.collection = db.restraunts
    
    def _format_document(self, doc):
        if doc and "_id" in doc:
            doc["id"] = str(doc.pop("_id"))
        return doc

    def create(self, restraunt: Restraunt) -> RestrauntResponse:
        data = restraunt.model_dump()
        result = self.collection.insert_one(data)
        
        # Create response data with the new id
        response_data = data.copy()
        response_data.pop("_id", None)  # Remove the ObjectId inserted by MongoDB
        response_data["id"] = str(result.inserted_id)
        return RestrauntResponse(**response_data)
    
    def get_all(self):
        docs = list(self.collection.find())
        if not docs:
            logger.info("No restaurants found in database")
            raise RestrauntNotFoundException("No restaurants found in database")
        return [self._format_document(doc) for doc in docs]
    
    def get_by_id(self, id: str):
        try:
            doc = self.collection.find_one({"_id": ObjectId(id)})
            if not doc:
                logger.error(f"Restraunt not found with id: {id}")
                raise RestrauntNotFoundException(f"Restraunt with id {id} not found")
            return self._format_document(doc)
        except InvalidId:
            logger.error(f"Invalid ObjectId string: {id}")
            raise RestrauntNotFoundException(f"Invalid restaurant id format: {id}")
    
    def update(self, id: str, restraunt: UpdateRestraunt):
        try:
            updated_data = {k: v for k, v in restraunt.model_dump().items() if v is not None}
            if updated_data:
                result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
                if result.matched_count == 0:
                    logger.error(f"Restraunt not found for update with id: {id}")
                    raise RestrauntNotFoundException(f"Restraunt with id {id} not found")
            return self.get_by_id(id)
        except InvalidId:
            logger.error(f"Invalid ObjectId string during update: {id}")
            raise RestrauntNotFoundException(f"Invalid restaurant id format during update: {id}")
    
    def delete(self, id: str):
        try:
            # We want to return the restaurant that was deleted
            # get_by_id will handle InvalidId and existence checks
            restraunt = self.get_by_id(id)
            self.collection.delete_one({"_id": ObjectId(id)})
            return restraunt
        except InvalidId:
            logger.error(f"Invalid ObjectId string during delete: {id}")
            raise RestrauntNotFoundException(f"Invalid restaurant id format during delete: {id}")
