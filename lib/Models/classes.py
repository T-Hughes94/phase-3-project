from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

class Food_Truck(Base):
    __tablename__ = 'food_truck'

    id = Column(Integer, primary_key= True)
    name = Column(String)

    
class Customer(Base):
    __tablename__ = 'customer'

