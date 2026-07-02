from pydantic import BaseModel


class BondResponse(BaseModel):
    id: str
    figi: str
    ticker: str
    name: str
    nominal_price: float
    current_price: float


class BondCreate(BaseModel):
    id: str
    figi: str
    ticker: str
    name: str
    nominal_price: float
    current_price: float
    