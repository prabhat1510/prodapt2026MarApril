from fastapi import APIRouter, HTTPException, Depends
from schemas import ItemCreate, ItemUpdate
from repository import ItemRepository
from service import ItemService
import invalidstockexception as ise
import itemnotfoundexception as infe

router = APIRouter(prefix="/items", tags=["Inventory"])

# Global repository and service instance for the in-memory store
repo = ItemRepository()
service = ItemService(repo)

def get_service() -> ItemService:
    return service

# 1. Add Item
@router.post("")
def add_item(item: ItemCreate, svc: ItemService = Depends(get_service)):
    try:
        return svc.add_item(item.item_id, item.name, item.price, item.quantity)
    except ise.InvalidStockException as e:
        raise HTTPException(status_code=400, detail=str(e))

# 2. Update Quantity
@router.put("/{item_id}")
def update_quantity(item_id: str, item_update: ItemUpdate, svc: ItemService = Depends(get_service)):
    try:
        return svc.update_quantity(item_id, item_update.quantity)
    except infe.ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ise.InvalidStockException as e:
        raise HTTPException(status_code=400, detail=str(e))

# 3. Remove Item
@router.delete("/{item_id}")
def remove_item(item_id: str, svc: ItemService = Depends(get_service)):
    try:
        return svc.remove_item(item_id)
    except infe.ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

# 4. View Inventory
@router.get("")
def view_inventory(svc: ItemService = Depends(get_service)):
    return svc.view_inventory()

# 5. Total Stock Value
@router.get("/stock/value")
def total_stock_value(svc: ItemService = Depends(get_service)):
    return svc.get_total_stock_value()

# 6. Low Stock Items
@router.get("/stock/low")
def low_stock_items(threshold: int = 5, svc: ItemService = Depends(get_service)):
    return svc.get_low_stock_items(threshold)
