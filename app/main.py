from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from .crud import *
from .database import SessionLocal, engine, Base
from .schemas import *

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/company/{name}", response_model=CompanySchema)
def get_company(name: str, db: Session = Depends(get_db)):
    db_company = get_company_by_name(db, name=name)
    if not db_company:
        raise HTTPException(status_code=409, detail="company don't exist")
    return db_company


@app.post("/company/", response_model=CompanySchema)
def post_company(company: CompanySchema, db: Session = Depends(get_db)):
    db_company = get_company_by_name(db, name=company.name)
    if db_company:
        raise HTTPException(status_code=409, detail="company already exist")
    return create_company(db=db, company=company)


@app.put("/company/", response_model=CompanySchema)
def put_company(company: CompanySchema, db: Session = Depends(get_db)):
    db_company = update_company(db, company=company)
    if not db_company:
        raise HTTPException(status_code=409, detail="company don't exist")
    return db_company


@app.delete("/company/{name}")
def delete_company(name: str, db: Session = Depends(get_db)):
    db_company = del_company(db, name=name)
    if not db_company:
        raise HTTPException(status_code=409, detail="company don't exist")
    return {"message": "Item deleted successfully"}


@app.get("/product/{name}", response_model=ProductSchema)
def get_product(name: str, db: Session = Depends(get_db)):
    db_product = get_product_by_name(db, name=name)
    if not db_product:
        raise HTTPException(status_code=409, detail="product don't exist")
    return db_product


@app.post("/product/", response_model=ProductSchema)
def post_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = get_product_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=409, detail="product already exist")
    return create_product(db=db, product=product)


@app.put("/product/", response_model=ProductSchema)
def put_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = update_product(db, product=product)
    if not db_product:
        raise HTTPException(status_code=409, detail="company don't exist")
    return db_product


@app.delete("/product/{name}")
def delete_product(name: str, db: Session = Depends(get_db)):
    db_product = del_product(db, name=name)
    if not db_product:
        raise HTTPException(status_code=409, detail="product don't exist")
    return {"message": "Item deleted successfully"}


@app.get("/company_products/")
def get_company_products(db: Annotated[Session, Depends(get_db)], company_id: int, offset: int = 0, limit: int = 10):
    return paginate_company_products(db, company_id, offset, limit)
