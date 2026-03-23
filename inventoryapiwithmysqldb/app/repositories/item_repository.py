from sqlalchemy.orm import Session
from app.models.item_model import Item

class ItemRepository:

    @staticmethod
    def create(db: Session, item):
        db_item = Item(name=item.name, price=item.price, quantity=item.quantity)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_all(db: Session):
        return db.query(Item).all()

    @staticmethod
    def get_by_id(db: Session, item_id: int):
        return db.query(Item).filter(Item.item_id == item_id).first()

    @staticmethod
    def delete(db: Session, item_id: int):
        item = db.query(Item).filter(Item.item_id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
        return item

    @staticmethod
    def update(db: Session, item_id: int, item):
        item = db.query(Item).filter(Item.item_id == item_id).first()
        if item:
            item.name = item.name
            item.price = item.price
            item.quantity = item.quantity
            db.commit()
            db.refresh(item)
        return item