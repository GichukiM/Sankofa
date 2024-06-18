# create_tables.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product, Supplier, Transaction

# Create the database engine
engine = create_engine('sqlite:///inventory.db')

# Bind the engine to the metadata of the Base class
Base.metadata.bind = engine

# Create all tables
Base.metadata.create_all(engine)
print("Tables created successfully!")
