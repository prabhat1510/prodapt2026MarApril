from bson import ObjectId
from bson.errors import InvalidId
from pymongo.database import Database
from app.core.logger import setup_logger
from app.schemas.customer_schema import Customer,CustomerResponse
from app.utils.exceptions import CustomerNotFoundException
logger = setup_logger()

class CustomerRepository:
    def __init__(self, db: Database):
        self.db = db
        self.collection = db.customers
    
    def _format_document(self, doc):
        if doc and "_id" in doc:
            doc["id"] = str(doc.pop("_id"))
        return doc

    def create(self, customer: Customer) -> CustomerResponse:
        data = customer.model_dump()
        result = self.collection.insert_one(data)
        
        # Create response data with the new id
        response_data = data.copy()
        response_data.pop("_id", None)  # Remove the ObjectId inserted by MongoDB
        response_data["id"] = str(result.inserted_id)
        return CustomerResponse(**response_data)
    
    def get_all(self):
        docs = list(self.collection.find())
        if not docs:
            logger.info("No customers found in database")
            raise CustomerNotFoundException("No customers found in database")
        return [self._format_document(doc) for doc in docs]
    
    def get_by_id(self, id: str):
        try:
            doc = self.collection.find_one({"_id": ObjectId(id)})
            if not doc:
                logger.error(f"Customer not found with id: {id}")
                raise CustomerNotFoundException(f"Customer with id {id} not found")
            return self._format_document(doc)
        except InvalidId:
            logger.error(f"Invalid ObjectId string: {id}")
            raise CustomerNotFoundException(f"Invalid customer id format: {id}")
    
    def update(self, id: str, customer: Customer):
        try:
            updated_data = {k: v for k, v in customer.model_dump().items() if v is not None}
            if updated_data:
                result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
                if result.matched_count == 0:
                    logger.error(f"Customer not found for update with id: {id}")
                    raise CustomerNotFoundException(f"Customer with id {id} not found")
            return self.get_by_id(id)
        except InvalidId:
            logger.error(f"Invalid ObjectId string during update: {id}")
            raise CustomerNotFoundException(f"Invalid customer id format during update: {id}")
    
    def delete(self, id: str):
        try:
            # We want to return the customer that was deleted
            # get_by_id will handle InvalidId and existence checks
            customer = self.get_by_id(id)
            self.collection.delete_one({"_id": ObjectId(id)})
            return customer
        except InvalidId:
            logger.error(f"Invalid ObjectId string during delete: {id}")
            raise CustomerNotFoundException(f"Invalid customer id format during delete: {id}")
