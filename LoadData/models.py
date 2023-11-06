"""
Database Model for Storing Laptop Data

This Python script defines the SQLAlchemy database model for storing laptop data. It creates a 'laptops' table with
various columns to represent laptop attributes. The model includes an 'id' column as the primary key.

Database Model:
- Laptop (SQLAlchemy model): Represents the 'laptops' table with columns for laptop details.

Attributes:
- id (int): Primary key for unique identification.
- model (str): Laptop model name (unique and required).
- brand (str): Laptop brand name.
- regular_price (float): Regular price of the laptop.
- special_price (float): Special price of the laptop.
- discount (float): Discount amount.
- processor_brand (str): Brand of the laptop's processor.
- processor_model (str): Model of the laptop's processor.
- processor_frequency (str): Processor base frequency.
- ram (str): RAM capacity.
- ram_type (str): RAM type.
- storage (str): Storage details.
- display_size (str): Display size.
- display_type (str): Display type.
- graphics_model (str): Graphics model.
- battery_type (str): Battery type.
- battery_capacity (str): Battery capacity.
- reviews (int): Number of reviews for the laptop.

Usage:
You can use this database model to store and retrieve laptop data in a relational database.

Author: [Abdul Ahad]
"""


from sqlalchemy import Column, Integer, String, Float, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from dbSettings import connection_string


engine = create_engine(connection_string)

Base = declarative_base()


class Laptop(Base):
    __tablename__ = 'laptops'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    model = Column(String, unique=True, nullable=False)
    brand = Column(String, nullable=True)
    regular_price = Column(Float, nullable=True)
    special_price = Column(Float, nullable=True)
    discount = Column(Float, nullable=True)
    processor_brand = Column(String, nullable=True)
    processor_model = Column(String, nullable=True)
    processor_frequency = Column(String, nullable=True)
    ram = Column(String, nullable=True)
    ram_type = Column(String, nullable=True)
    storage = Column(String, nullable=True)
    display_size = Column(String, nullable=True)
    display_type = Column(String, nullable=True)
    graphics_model = Column(String, nullable=True)
    battery_type = Column(String, nullable=True)
    battery_capacity = Column(String, nullable=True)
    reviews = Column(Integer, nullable=True)

    def __str__(self):
        return str(self.model)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
