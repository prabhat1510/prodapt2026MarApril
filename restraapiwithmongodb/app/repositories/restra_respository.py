from app.schemas.schemas import Restraunt, UpdateRestraunt
from bson import ObjectId
from pymongo.database import Database

class RestrauntRepository:
    def __init__(self, db: Database):
        self.db = db
        self.collection = db.restraunts
    
    def _format_document(self, doc):
        if doc and "_id" in doc:
            doc["_id"] = str(doc["_id"])
        return doc

    def create(self, restraunt: Restraunt):
        data = restraunt.model_dump(exclude={"id"})
        result = self.collection.insert_one(data)
        restraunt.id = str(result.inserted_id)
        return restraunt
    
    def get_all(self):
        docs = list(self.collection.find())
        return [self._format_document(doc) for doc in docs]
    
    def get_by_id(self, id: str):
        doc = self.collection.find_one({"_id": ObjectId(id)})
        return self._format_document(doc)
    
    def update(self, id: str, restraunt: UpdateRestraunt):
        updated_data = {k: v for k, v in restraunt.model_dump().items() if v is not None}
        if updated_data:
            self.collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return self.get_by_id(id)
    
    def delete(self, id: str):
        restraunt = self.get_by_id(id)
        if restraunt:
            self.collection.delete_one({"_id": ObjectId(id)})
        return restraunt
