from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, declarative_base
# from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Food_Truck(Base):
    __tablename__ = 'food_truck'

    id = Column(Integer, primary_key= True)
    name = Column(String)
    food_type = Column(String)

    
class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key= True)
    name = Column(String)

