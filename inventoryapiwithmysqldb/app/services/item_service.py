from sqlalchemy.orm import Session
from app.repositories.item_repository import ItemRepository
from app.utils.exceptions import ItemNotFoundException, InvalidStockException

class ItemService:

    @staticmethod
    def create_item(db: Session, item):
        if item.quantity < 0:
            raise InvalidStockException("Quantity cannot be negative")
        if item.price < 0:
            raise InvalidStockException("Price cannot be negative")
        return ItemRepository.create(db, item)

    @staticmethod
    def get_items(db: Session):
        return ItemRepository.get_all(db)

    @staticmethod
    def get_item(db: Session, item_id: int):
        item = ItemRepository.get_by_id(db,item_id)
        
        if not item:
            raise ItemNotFoundException("Item not found")
        return item

    @staticmethod
    def delete_item(db: Session, item_id: int):
        item = ItemRepository.delete(db, item_id)
        if not item:
            raise ItemNotFoundException("Item not found")
        return item

    @staticmethod
    def update_item(db: Session, item_id: int, item):
        if item.quantity < 0:
            raise InvalidStockException("Quantity cannot be negative")
        if item.price < 0:
            raise InvalidStockException("Price cannot be negative")
        item = ItemRepository.update(db, item_id, item)
        if not item:
            raise ItemNotFoundException("Item not found")
        return item