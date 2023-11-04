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
        return self.model


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
