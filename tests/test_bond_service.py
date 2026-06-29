import pytest

from services.bond_service import get_all_bonds, search_bonds, get_bond_by_id


def test_get_all_bonds_returns_list():
    result = get_all_bonds()
    assert isinstance(result, list)


@pytest.mark.parametrize("ticker", ["RU000A1076A0", "RU000A10B4L1"])
def test_search_bonds_finds_by_ticker(ticker):
    result = search_bonds(ticker)
    assert len(result) > 0, f"Тикер {ticker} отсутствует"


def test_search_bonds_returns_empty_for_missing_ticker(ticker="RU000A1076A1"):
    result = search_bonds(ticker)
    assert len(result) == 0, f"Тикер {ticker} есть, используй для проверки test_search_bonds_finds_by_ticker"


def test_get_bond_by_id_raises_error_on_missing(bond_id="6"):
    with pytest.raises(KeyError) as exc_info:
        get_bond_by_id(bond_id)
    assert "не найдена" in str(exc_info.value)
