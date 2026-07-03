from repository.json_repo import load_bonds, save_bonds


def get_all_bonds() -> list[dict]:
    """
    Получить все облигации.
    Returns:
        list[dict]: Список облигаций.
    """
    return load_bonds()


def get_bond_by_id(bond_id: str) -> dict:
    """
    Получить облигацию по id.
    Args:
        bond_id (str): Идентификатор облигации.
    Returns:
        dict: Облигация.
    Raises:
        KeyError: Если облигация с указанным id не найдена.
    """
    index = _build_bond_index()
    try:
        return index[bond_id]
    except KeyError:
        raise KeyError(f"Облигация с id {bond_id} не найдена")


def add_bond(bond_data: dict) -> dict:
    """
    Добавить облигацию.
    Args:
        bond_data (dict): Облигация.
    Returns:
        dict: Добавленная облигация.
    """
    bonds = get_all_bonds()
    bond_copy = bond_data.copy()
    bonds.append(bond_copy)
    save_bonds(bonds=bonds)
    return bond_copy


def search_bonds(keyword: str) -> list[dict]:
    """
    Найти облигации по ключевому слову (поиск по имени и тикеру).
    Args:
        keyword (str): Ключевое слово.
    Returns:
        list[dict]: Список облигаций.
    """
    bonds = get_all_bonds()
    result = [bond for bond in bonds if
              keyword.lower() in bond["name"].lower() or keyword.lower() in bond["ticker"].lower()]
    return result


def _build_bond_index() -> dict[str, dict]:
    """
    Создать индексы облигаций.
    Returns:
        dict[str, dict]: Словарь облигаций.
    """
    bonds = get_all_bonds()
    return {bond["id"]: bond for bond in bonds}


def get_unique_tickers() -> set[str]:
    """
    Получить уникальные тикеры облигаций.
    Returns:
        set[str]: Множество тикеров.
    """
    bonds = get_all_bonds()
    return {bond["ticker"] for bond in bonds}


def remove_bond(bond_id: str) -> None:
    """
    Удалить облигацию по id.
    Args:
        bond_id (str): Идентификатор облигации.
    Raises:
        KeyError: Если облигация с указанным id не найдена.
    """
    bonds = get_all_bonds()
    new_bonds = [bond for bond in bonds if bond["id"]!=bond_id]
    if len(bonds) == len(new_bonds):
        raise KeyError(f"Облигация с id {bond_id} не найдена")
    else:
        save_bonds(bonds=new_bonds)
