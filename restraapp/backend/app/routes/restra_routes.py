from fastapi import APIRouter,Depends,HTTPException
from app.schemas.restra_schema import Restraunt, UpdateRestraunt, RestrauntResponse
from app.services.restra_service import RestrauntService
from app.db.database import get_database
from app.utils.auth_dependency import get_current_user, require_role
from typing import List

router=APIRouter(prefix="/restraunt", tags=["Restraunt"])

@router.post("/create", response_model=RestrauntResponse)
def create_restraunt(restraunt: Restraunt, db=Depends(get_database), user=Depends(require_role(["admin","owner"]))):
    return RestrauntService(db).create_restraunt(restraunt, user["sub"])

@router.get("/getall", response_model=List[RestrauntResponse])
def get_all_restraunts(db=Depends(get_database)):
    return RestrauntService(db).get_all_restraunts()


@router.get("/getbyid/{id}", response_model=RestrauntResponse)
def get_restraunt(id: str, db=Depends(get_database), user=Depends(require_role(['admin','owner']))):
    return RestrauntService(db).get_restraunt(id)

@router.put("/update/{id}", response_model=RestrauntResponse)
def update_restraunt(id: str, restraunt: UpdateRestraunt, db=Depends(get_database), user=Depends(require_role(['admin','owner']))):
    return RestrauntService(db).update_restraunt(id, restraunt)

@router.delete("/delete/{id}", response_model=RestrauntResponse)
def delete_restraunt(id: str, db=Depends(get_database), user=Depends(require_role(['admin']))):
    return RestrauntService(db).delete_restraunt(id)
