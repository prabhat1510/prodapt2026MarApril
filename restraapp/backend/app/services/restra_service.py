from app.schemas.restra_schema import Restraunt, UpdateRestraunt,RestrauntResponse
from app.repositories.restra_repository import RestrauntRepository
from app.repositories.user_repository import UserRepository

class RestrauntService:
    def __init__(self, db):
        # We initialize the repository within the service
        self.repository = RestrauntRepository(db)
        self.user_repository = UserRepository(db)
    
    def create_restraunt(self, restraunt: Restraunt, username: str):
        # 1. Get the current user's ID
        user = self.user_repository.get_user_by_username(username)
        if not user:
            raise Exception("User not found")
        
        # 2. Assign the owner_id to the restaurant
        restraunt.owner_id = user["id"]
        
        # 3. Save the restaurant
        response = self.repository.create(restraunt)
        
        # 4. Link the restaurant to the user
        self.user_repository.add_restaurant_to_user(user["id"], response.id)
        
        return response
    
    def get_all_restraunts(self):
        return self.repository.get_all()
    
    def get_restraunt(self, id: str):
        return self.repository.get_by_id(id)
    
    def update_restraunt(self, id: str, restraunt: UpdateRestraunt):
        return self.repository.update(id, restraunt)
    
    def delete_restraunt(self, id: str):
        return self.repository.delete(id)