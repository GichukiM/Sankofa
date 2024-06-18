# transaction.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import engine, Session
from utils import validate_quantity
from product import Product
from supplier import Supplier

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    product = relationship("Product", back_populates="transactions")
    supplier = relationship("Supplier", back_populates="transactions")

    def __repr__(self):
        return f"Transaction(id={self.id}, product_id={self.product_id}, supplier_id={self.supplier_id}, quantity={self.quantity})"

Base.metadata.create_all(engine)

class TransactionManager:

    @staticmethod
    def record_transaction():
        session = Session()
        print("Recording Supply Transaction")
        print("===========================")
        product_name = input("Enter the name of the product: ")
        supplier_name = input("Enter the name of the supplier: ")
        quantity = input("Enter the quantity supplied: ")

        if validate_quantity(quantity):
            product = session.query(Product).filter_by(name=product_name).first()
            supplier = session.query(Supplier).filter_by(name=supplier_name).first()
            if product and supplier:
                transaction = Transaction(product_id=product.id, supplier_id=supplier.id, quantity=int(quantity))
                session.add(transaction)
                session.commit()
                print("Supply transaction recorded successfully!")
            else:
                print("Product or Supplier not found.")
        else:
            print("Invalid quantity.")
        session.close()

    @staticmethod
    def view_transactions():
        session = Session()
        print('Transaction History')
        print('===================')
        transactions = session.query(Transaction).all()
        for transaction in transactions:
            # Access product and supplier attributes through relationships
            print(f"Product: {transaction.product.name}")
            print(f"Supplier: {transaction.supplier.name}")
            print(f"Quantity: {transaction.quantity}")
            print('----------')
        session.close()
