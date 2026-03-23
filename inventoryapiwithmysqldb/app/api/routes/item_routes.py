from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.item_schema import ItemCreate, ItemResponse
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return ItemService.create_item(db, item)

@router.get("/", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return ItemService.get_items(db)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return ItemService.get_item(db, item_id)

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return ItemService.delete_item(db, item_id)

@router.put("/{item_id}")
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    return ItemService.update_item(db, item_id, item)