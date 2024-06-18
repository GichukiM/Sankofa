# supplier.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import engine, Session
from utils import validate_non_empty

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)

    def __repr__(self):
        return f"Supplier(name={self.name}, contact_info={self.contact_info})"

Base.metadata.create_all(engine)

class SupplierManager:

    @staticmethod
    def add_supplier():
        session = Session()
        print("Adding Supplier")
        print("================")
        name = input("Enter the name of the supplier: ")
        contact_info = input("Enter the contact information of the supplier: ")
        
        if validate_non_empty(name) and validate_non_empty(contact_info):
            supplier = Supplier(name=name, contact_info=contact_info)
            session.add(supplier)
            session.commit()
            print("Supplier added successfully!")
        else:
            print("Invalid input. Supplier not added.")
        session.close()

    @staticmethod
    def remove_supplier():
        session = Session()
        print("Removing Supplier")
        print("==================")
        name = input("Enter the name of the supplier to remove: ")

        supplier = session.query(Supplier).filter_by(name=name).first()
        if supplier:
            session.delete(supplier)
            session.commit()
            print("Supplier removed successfully!")
        else:
            print("Supplier not found.")
        session.close()

    @staticmethod
    def search_supplier():
        session = Session()
        print('Searching Supplier')
        print('===================')
        name = input('Enter the name of the supplier: ')

        supplier = session.query(Supplier).filter_by(name=name).first()
        if supplier:
            print(f"Supplier: {supplier.name}")
            print(f"Contact Info: {supplier.contact_info}")
        else:
            print("Supplier not found.")
        session.close()

    @staticmethod
    def print_suppliers():
        session = Session()
        print('Current Suppliers')
        print('-----------------')
        suppliers = session.query(Supplier).all()
        for supplier in suppliers:
            print(f"Supplier: {supplier.name}")
            print(f"Contact Info: {supplier.contact_info}")
            print('----------')
        session.close()