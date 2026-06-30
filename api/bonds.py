from fastapi import APIRouter

from api.schemas import BondResponse
from services.bond_service import get_all_bonds

router = APIRouter()


@router.get("/bonds")
def get_bonds() -> list[BondResponse]:
    bonds_dicts = get_all_bonds()
    return [BondResponse.model_validate(bond) for bond in bonds_dicts]
