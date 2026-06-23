from repository.json_repo import load_bonds, save_bonds


def get_all_bonds() -> list[dict]:
    return load_bonds()


def get_bond_by_id(bond_id: str) -> dict:
    bonds = get_all_bonds()
    for bond in bonds:
        if bond_id == bond["id"]:
            return bond
    raise KeyError(f"Облигация с id {bond_id} не найдена")


def add_bond(bond_data: dict) -> dict:
    bonds = get_all_bonds()
    bond_copy = bond_data.copy()
    bonds.append(bond_copy)
    save_bonds(bonds=bonds)
    return bond_copy


def search_bonds(keyword: str) -> list[dict]:
    bonds = get_all_bonds()
    result = [bond for bond in bonds if
              keyword.lower() in bond["name"].lower() or keyword.lower() in bond["ticker"].lower()]
    return result
