from typing import List, Optional
from item import Item

class ItemRepository:
    def __init__(self):
        # The in-memory data store acts as our database
        self.inventory = {}

    def get_all(self) -> List[Item]:
        return list(self.inventory.values())

    def get_by_id(self, item_id: str) -> Optional[Item]:
        return self.inventory.get(item_id)

    def add(self, item: Item) -> Item:
        self.inventory[item.item_id] = item
        return item

    def update(self, item: Item) -> Item:
        self.inventory[item.item_id] = item
        return item

    def delete(self, item_id: str) -> bool:
        if item_id in self.inventory:
            del self.inventory[item_id]
            return True
        return False
