# Bond Portfolio API

Backend service for bond portfolio management. Currently a prototype using JSON as a storage, with a planned migration to PostgreSQL and FastAPI in the future.
## Tech Stack

- Python 3.13
- JSON
- Git
- Pydantic
- uv


## Project Structure
```text
bond_portfolio_api/
├── .gitignore
├── README.md
├── main.py
├── api/
│   ├── __init__.py
│   ├── bonds.py
│   └── schemas.py
├── core/
│   ├── __init__.py
│   ├── app.py
│   └── decorators.py
├── data/
│   └── bonds.json
├── domain/
│   └── __init__.py
├── repository/
│   ├── __init__.py
│   └── json_repo.py
├── services/
│   ├── __init__.py
│   └── bond_service.py
└── tests/
    ├── __init__.py
    └── test_bond_service.py
```

## How to run
1. Clone the repository
2. Install uv
3. Install dependencies: uv sync
4. Run API: uv run python main.py
5. Run tests: `uv run pytest -v`
