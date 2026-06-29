from services.bond_service import add_bond, get_bond_by_id, get_all_bonds, search_bonds, get_unique_tickers

BOND_DATA =     {
        "id": "5",
        "figi": "BBG00000005",
        "ticker": "RU000A105LS2",
        "name": "Реиннольц 001Р-02",
        "nominal_price": 1000.00,
        "current_price": 984.50
    }

if __name__ == '__main__':
    print(get_all_bonds())
    print(get_bond_by_id(bond_id="1"))
    try:
        get_bond_by_id(bond_id="6")
    except KeyError as e:
        print(e)
    print(add_bond(bond_data=BOND_DATA))
    assert len(get_all_bonds()) > 0, "Список облигаций пуст"
    assert get_bond_by_id("1")["ticker"] is not None, "Нет тикера у облигации"
    print(search_bonds("ПЕТРО 001Р-01"))
    print(get_unique_tickers())
