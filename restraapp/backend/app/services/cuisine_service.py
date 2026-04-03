from app.schemas.cuisine_schema import Cuisine, UpdateCuisine, CuisineResponse
from app.repositories.cuisine_repository import CuisineRepository

class CuisineService:
    def __init__(self, db):
        # We initialize the repository within the service
        self.repository = CuisineRepository(db)
    
    def create_cuisine(self, cuisine: Cuisine):
        return self.repository.create(cuisine)
    
    def get_all_cuisines(self):
        return self.repository.get_all()
    
    def get_cuisine(self, id: str):
        return self.repository.get_by_id(id)
    
    def update_cuisine(self, id: str, cuisine: UpdateCuisine):
        return self.repository.update(id, cuisine)
    
    def delete_cuisine(self, id: str):
        return self.repository.delete(id)