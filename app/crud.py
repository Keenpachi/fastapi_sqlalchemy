from sqlalchemy.orm import Session
from .models import *
from .schemas import *


def get_company_by_name(db: Session, name: str):
    return db.query(Company).filter(Company.name == name).first()


def create_company(db: Session, company: CompanySchema):
    db_company = Company(name=company.name, address=company.address, contact=company.contact)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update_company(db: Session, company: CompanySchema):
    db_company = db.query(Company).filter(Company.name == company.name).one_or_none()
    if db_company is None:
        return None

    for var, value in vars(company).items():
        setattr(db_company, var, value) if value else None

    db.commit()
    db.refresh(db_company)
    return db_company


def del_company(db: Session, name: str):
    db_company = db.query(Company).filter(Company.name == name).first()
    db.delete(db_company)
    db.commit()
    return True


def get_product_by_name(db: Session, name: str):
    return db.query(Product).filter(Product.name == name).first()


def create_product(db: Session, product: ProductSchema):
    db_product = Product(name=product.name, description=product.description, price=product.price, available=product.available, company_id=product.company_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product: ProductSchema):
    db_product = db.query(Product).filter(Product.name == product.name).one_or_none()
    if db_product is None:
        return None

    for var, value in vars(product).items():
        setattr(db_product, var, value) if value else None

    db.commit()
    db.refresh(db_product)
    return db_product


def del_product(db: Session, name: str):
    db_product = db.query(Product).filter(Product.name == name).first()
    db.delete(db_product)
    db.commit()
    return True


def get_all_company_products(db: Session, company_id: int):
    db_products = db.query(Product).filter(Product.company_id == company_id).all()
    return db_products

