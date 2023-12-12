#This file creates the data and establishes relationships between the tables
from sqlalchemy import Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import declarative_base, relationship, validates



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

    @validates("name")
    def validate_name(self, key, name):
        if isinstance(name, str) and len(name) > 0:
            return name
        else:
            raise ValueError("Not a valid name")


    def __repr__(self):
        return f'{self.name}'


class Order(Base):
    __tablename__ = 'order'
    #gives this table/class a unique id 
    id = Column(Integer, primary_key= True)
    order_number = Column(Integer)
    
    #foreign keys to connect Food_Truck and Customer objects to the Order object
    food_truck_id = Column(Integer, ForeignKey('food_truck.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    #relationships between Order and Classes listed in relationship instances below
    customer = relationship('Customer', backref= "orders")#creates a connection into Customer Class from the Order Class
    food_truck = relationship('Food_Truck', backref= "orders")

class Menu_Order(Base):
    __tablename__ = 'menu_order'

    id = Column(Integer, primary_key= True)
    quantity = Column(Integer)
    
    order_id = Column(Integer, ForeignKey('order.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_item.id'))

   
    menu_items = relationship('Menu_Item', backref = "menu_orders")
    order = relationship('Order', backref = "menu-orders")

class Menu_Item(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key= True)
    item = Column(String)
    description = Column(String)
    price = Column(Float)

    food_truck_id = Column(Integer, ForeignKey('food_truck.id'))

    food_trucks = relationship('Food_Truck', backref= "menu_items")

