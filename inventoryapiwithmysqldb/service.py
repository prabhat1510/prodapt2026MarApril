from repository import ItemRepository
from item import Item
import invalidstockexception as ise
import itemnotfoundexception as infe
from typing import List, Dict

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def add_item(self, item_id: str, name: str, price: float, quantity: int) -> Dict[str, str]:
        if price <= 0 or quantity < 0:
            raise ise.InvalidStockException("Invalid price or quantity")

        if self.repository.get_by_id(item_id):
            raise ise.InvalidStockException("Item already exists")

        new_item = Item(item_id, name, price, quantity)
        self.repository.add(new_item)
        return {"message": "Item added successfully."}

    def update_quantity(self, item_id: str, quantity: int) -> Dict[str, str]:
        item = self.repository.get_by_id(item_id)
        if not item:
            raise infe.ItemNotFoundException("Item not found")

        if quantity < 0:
            raise ise.InvalidStockException("Quantity cannot be negative")

        item.quantity = quantity
        self.repository.update(item)
        return {"message": "Quantity updated successfully."}

    def remove_item(self, item_id: str) -> Dict[str, str]:
        if not self.repository.get_by_id(item_id):
            raise infe.ItemNotFoundException("Item not found")

        self.repository.delete(item_id)
        return {"message": "Item removed successfully."}

    def view_inventory(self) -> Dict[str, any]:
        items = self.repository.get_all()
        if not items:
            return {"message": "Inventory is empty.", "inventory": []}

        # Convert objects to dictionaries
        inventory_list = [
            {
                "item_id": i.item_id,
                "name": i.name,
                "price": i.price,
                "quantity": i.quantity,
                "stock_value": i.get_stock_value()
            } for i in items
        ]
        return {"inventory": inventory_list}

    def get_total_stock_value(self) -> Dict[str, float]:
        total = sum(item.get_stock_value() for item in self.repository.get_all())
        return {"total_stock_value": total}

    def get_low_stock_items(self, threshold: int = 5) -> Dict[str, any]:
        items = self.repository.get_all()
        low_stock = [
            {
                "item_id": i.item_id,
                "name": i.name,
                "price": i.price,
                "quantity": i.quantity
            } for i in items if i.quantity <= threshold
        ]
        return {"low_stock_items": low_stock}
