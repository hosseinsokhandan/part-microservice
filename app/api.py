from typing import List
from fastapi import APIRouter, HTTPException
from schemas import PartOutSchema
from services import part_service


router = APIRouter()


@router.get("/automobile/{id}", response_model=List[PartOutSchema])
def get_by_automobile_id(id: int):
    parts: List[dict] = part_service.get_by_automobile_id(id)
    print(parts)
    return parts


@router.get("/{id}", response_model=PartOutSchema)
def get(id: int):
    parts = part_service.get(id)
    if parts:
        return PartOutSchema.parse_obj(parts[0])
    raise HTTPException(status_code=404)
