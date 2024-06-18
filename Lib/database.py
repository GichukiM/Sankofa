# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URI
DATABASE_URI = 'sqlite:///inventory.db'

# Create the engine
engine = create_engine(DATABASE_URI)

# Create the session
Session = sessionmaker(bind=engine)
