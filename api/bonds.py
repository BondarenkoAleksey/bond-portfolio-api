from fastapi import APIRouter, HTTPException, status

from api.schemas import BondResponse, BondCreate
from services.bond_service import get_all_bonds, get_bond_by_id, add_bond, remove_bond

router = APIRouter()


@router.get("/bonds")
def get_bonds() -> list[BondResponse]:
    """Получение списка облигаций."""
    bonds_dicts = get_all_bonds()
    return [BondResponse.model_validate(bond) for bond in bonds_dicts]


@router.get("/bonds/{bond_id}")
def get_bond(bond_id: str) -> BondResponse:
    """Получение облигации по id."""
    try:
        bond = get_bond_by_id(bond_id)
        result = BondResponse.model_validate(bond)
        return result
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/bonds", status_code=status.HTTP_201_CREATED)
def create_bond(bond_data: BondCreate) -> BondResponse:
    """Создание новой облигации."""
    bond_dict = bond_data.model_dump()
    new_bond = add_bond(bond_dict)
    return BondResponse.model_validate(new_bond)


@router.delete("/bonds/{bond_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bond(bond_id: str) -> None:
    """Удаление облигации по id."""
    try:
        remove_bond(bond_id)
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
