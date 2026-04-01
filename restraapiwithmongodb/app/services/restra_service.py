from app.schemas.schemas import Restraunt, UpdateRestraunt
from app.repositories.restra_respository import RestrauntRepository

class RestrauntService:
    def __init__(self, db):
        # We initialize the repository within the service
        self.repository = RestrauntRepository(db)
    
    def create_restraunt(self, restraunt: Restraunt):
        return self.repository.create(restraunt)
    
    def get_all_restraunts(self):
        return self.repository.get_all()
    
    def get_restraunt(self, id: str):
        return self.repository.get_by_id(id)
    
    def update_restraunt(self, id: str, restraunt: UpdateRestraunt):
        return self.repository.update(id, restraunt)
    
    def delete_restraunt(self, id: str):
        return self.repository.delete(id)