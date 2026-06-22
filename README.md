# Bond Portfolio API

Backend service for bond portfolio management.Currently a prototype using JSON as a storage, with a planned migration to PostgreSQL and FastAPI in the future.
## Tech Stack

- Python 3.13
- JSON
- Git


## Project Structure
```text
bond_portfolio_api/
├── .gitignore
├── README.md
├── main.py
├── data/
│   └── bonds.json
├── domain/
│   └── __init__.py
├── repository/
│   ├── __init__.py
│   └── json_repo.py
└── services/
    ├── __init__.py
    └── bond_service.py
```

## How to run
1. Clone the repository

2. Create and activate a virtual environment

3. Run python main.py
