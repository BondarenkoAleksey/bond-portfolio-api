from fastapi.testclient import TestClient
from core.app import app

TEST_BOND = {
        "id": "12345",
        "figi": "BBG00012345",
        "ticker": "RU000A106WZ2",
        "name": "АПРИ БО-002Р-03",
        "nominal_price": 1000.0,
        "current_price": 984.6
    }

def client():
    return TestClient(app)

def test_get_bonds_returns_200():
    response = client().get("/bonds")
    assert  response.status_code == 200, f"Ожидаемый статус-код 200, фактический статус-код - {response.status_code}"
    assert isinstance(response.json(), list), f"Неверный тип данных в JSON"


def test_get_bond_by_id_returns_404():
    get_response = client().get("/bonds/9999")
    assert  get_response.status_code == 404, \
        f"Ожидаемый статус-код 404, фактический статус-код - {get_response.status_code}"


def test_create_and_delete_bond():
    bond_id = TEST_BOND["id"]
    post_response = client().post("/bonds", json=TEST_BOND)
    assert post_response.status_code == 201
    get_response = client().get(f"/bonds/{bond_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == TEST_BOND["name"]
    delete_response = client().delete(f"/bonds/{bond_id}")
    assert delete_response.status_code == 204
    get_response = client().get(f"/bonds/{bond_id}")
    assert get_response.status_code == 404
