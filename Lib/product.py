# product.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import engine, Session
from utils import validate_non_empty, validate_quantity

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Product(name={self.name}, quantity={self.quantity})"

Base.metadata.create_all(engine)

class ProductManager:

    @staticmethod
    def add_product():
        session = Session()
        print("Adding Product")
        print("================")
        name = input("Enter the name of the product: ")
        quantity = input("Enter the quantity of the product: ")
        
        if validate_non_empty(name) and validate_quantity(quantity):
            product = Product(name=name, quantity=int(quantity))
            session.add(product)
            session.commit()
            print("Product added successfully!")
        else:
            print("Invalid input. Product not added.")
        session.close()

    @staticmethod
    def remove_product():
        session = Session()
        print("Removing Product")
        print("==================")
        name = input("Enter the name of the product to remove: ")

        product = session.query(Product).filter_by(name=name).first()
        if product:
            session.delete(product)
            session.commit()
            print("Product removed successfully!")
        else:
            print("Product not found.")
        session.close()

    @staticmethod
    def update_product():
        session = Session()
        print("Updating Product")
        print("==================")
        name = input('Enter the name of the product to update: ')
        quantity = input("Enter the updated quantity: ")

        if validate_quantity(quantity):
            product = session.query(Product).filter_by(name=name).first()
            if product:
                product.quantity = int(quantity)
                session.commit()
                print("Product updated successfully!")
            else:
                print("Product not found.")
        else:
            print("Invalid quantity.")
        session.close()

    @staticmethod
    def search_product():
        session = Session()
        print('Searching Product')
        print('===================')
        name = input('Enter the name of the product: ')

        product = session.query(Product).filter_by(name=name).first()
        if product:
            print(f"Product: {product.name}")
            print(f"Quantity: {product.quantity}")
        else:
            print("Product not found.")
        session.close()

    @staticmethod
    def print_inventory():
        session = Session()
        print('Current Inventory')
        print('-----------------')
        products = session.query(Product).all()
        for product in products:
            print(f"Product: {product.name}")
            print(f"Quantity: {product.quantity}")
            print('----------')
        session.close()
