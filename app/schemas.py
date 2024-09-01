from pydantic import BaseModel


class CompanySchema(BaseModel):
    id: int
    name: str
    address: str
    contact: str

    class Config:
        orm_mode = True


class ProductSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float
    available: bool
    company_id: int

    class Config:
        orm_mode = True
