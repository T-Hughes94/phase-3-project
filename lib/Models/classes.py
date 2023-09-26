#This file creates the data and establishes relationships between the tables
from sqlalchemy import Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship, validates
# from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Food_Truck(Base):
    __tablename__ = 'food_truck'

    id = Column(Integer, primary_key= True)
    name = Column(String)
    food_type = Column(String)

    @validates("name")
    def validate_name(self, key, name):
        if isinstance(name, str) and len(name) > 0:
            return name
        else:
            raise ValueError("Not a valid name")

     
    def __repr__(self):
        return f'{self.name}'
    
class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key= True)
    name = Column(String)


    def __repr__(self):
        return f'{self.name}'


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key= True)
    order_number = Column(Integer)
    food_truck_id = Column(Integer, ForeignKey('food_truck.id'))
    food_truck = relationship('Food_Truck', backref= "orders")
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer', backref= "orders")


class Menu_Order(Base):
    __tablename__ = 'menu_order'

    id = Column(Integer, primary_key= True)
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship('Order', backref = "menu-orders")
    menu_item_id = Column(Integer, ForeignKey('menu_item.id'))
    menu_items = relationship('Menu_Item', backref = "menu_orders")
    quantity = Column(Integer)


class Menu_Item(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key= True)
    item = Column(String)
    description = Column(String)
    food_truck_id = Column(Integer, ForeignKey('food_truck.id'))
    food_trucks = relationship('Food_Truck', backref= "menu_items")
    price = Column(Float)

