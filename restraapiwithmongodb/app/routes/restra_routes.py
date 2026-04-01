from fastapi import APIRouter,Depends,HTTPException
from app.schemas.schemas import Restraunt,UpdateRestraunt
from app.services.restra_service import RestrauntService
from app.db.database import get_database
from typing import List

router=APIRouter()

@router.post("/create", response_model=Restraunt)
def create_restraunt(restraunt: Restraunt, db=Depends(get_database)):
    return RestrauntService(db).create_restraunt(restraunt)

@router.get("/getall", response_model=List[Restraunt])
def get_all_restraunts(db=Depends(get_database)):
    return RestrauntService(db).get_all_restraunts()


@router.get("/getbyid/{id}", response_model=Restraunt)
def get_restraunt(id: str, db=Depends(get_database)):
    return RestrauntService(db).get_restraunt(id)

@router.put("/update/{id}", response_model=Restraunt)
def update_restraunt(id: str, restraunt: UpdateRestraunt, db=Depends(get_database)):
    return RestrauntService(db).update_restraunt(id, restraunt)

@router.delete("/delete/{id}", response_model=Restraunt)
def delete_restraunt(id: str, db=Depends(get_database)):
    return RestrauntService(db).delete_restraunt(id)
