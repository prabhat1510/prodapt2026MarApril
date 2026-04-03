from fastapi import APIRouter,Depends,HTTPException
from app.schemas.cuisine_schema import Cuisine, UpdateCuisine, CuisineResponse
from app.services.cuisine_service import CuisineService
from app.db.database import get_database
from app.utils.auth_dependency import get_current_user, require_role
from typing import List

router=APIRouter(prefix="/cuisine", tags=["Cuisine"])

@router.post("/create", response_model=CuisineResponse)
def create_cuisine(cuisine: Cuisine, db=Depends(get_database), user=Depends(require_role(['owner']))):
    return CuisineService(db).create_cuisine(cuisine)

@router.get("/getall", response_model=List[CuisineResponse])
def get_all_cuisines(db=Depends(get_database)):
    return CuisineService(db).get_all_cuisines()


@router.get("/getbyid/{id}", response_model=CuisineResponse)
def get_cuisine(id: str, db=Depends(get_database), user=Depends(require_role(['owner']))):
    return CuisineService(db).get_cuisine(id)

@router.put("/update/{id}", response_model=CuisineResponse)
def update_cuisine(id: str, cuisine: UpdateCuisine, db=Depends(get_database), user=Depends(require_role(['owner']))):
    return CuisineService(db).update_cuisine(id, cuisine)

@router.delete("/delete/{id}", response_model=CuisineResponse)
def delete_cuisine(id: str, db=Depends(get_database), user=Depends(require_role(['owner']))):
    return CuisineService(db).delete_cuisine(id)