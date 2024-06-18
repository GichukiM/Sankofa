# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Product(name={self.name}, quantity={self.quantity})"

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)

    def __repr__(self):
        return f"Supplier(name={self.name}, contact_info={self.contact_info})"

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    product = relationship("Product")
    supplier = relationship("Supplier")

    def __repr__(self):
        return f"Transaction(product={self.product.name}, supplier={self.supplier.name}, quantity={self.quantity})"
