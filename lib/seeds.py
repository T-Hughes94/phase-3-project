#this file creates the data to be used in the CLI
# from Models.classes import Food_Truck, Customer, Order, Menu_Item, Menu_Order, Base, Session as ORM_Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session

from Models.classes import Food_Truck, Customer, Order, Menu_Item, Menu_Order, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as ORM_Session




if __name__ == "__main__":
   
    engine = create_engine('sqlite:///food_truck.db')
    
    # Food_Truck.__table__.drop(engine)
    # Customer.__table__.drop(engine)
    # Order.__table__.drop(engine)
    # Menu_Item.__table__.drop(engine)
    # Menu_Order.__table__.drop(engine)

    # Base.metadata.create_all(engine)
    
    # with Session(engine) as session:
    with ORM_Session(engine) as session:
        #create food trucks
        truck1 = Food_Truck(name = "Eazy T's", food_type = "American & Mexican Fusion")
        truck2 = Food_Truck(name = "Taste of Santo Domingo", food_type = "Dominican")
        truck3 = Food_Truck(name = "Baran's Hot-Dogs" , food_type = "Multi-Cultural")
        #create customers
        cust1 = Customer(name = "John")    
        cust2 = Customer(name = "Sally")
        cust3 = Customer(name = "Rick")
        #create menu items for each truck
        #Food Truck 1
        item1 = Menu_Item(item = "Juan-tons", description = "Tasty fried green chili snack" ,food_trucks = truck1, price = 15)
        item2 = Menu_Item(item = "Slopper", description = "Cheesburger smothered with green chili", food_trucks = truck1, price = 15)
        item3 = Menu_Item(item = "Green Chili Dog", description = "Hot dog smothered with green chili, topped with fritos and cheese", food_trucks = truck1, price = 10)
        #Food Truck 2
        item4 = Menu_Item(item = "Mangu", description = "Mashed plantains served wtih Fried eggs & Fried Salami", food_trucks = truck2, price = 12)
        item5 = Menu_Item(item = "Habichuelas Guisadas con Carne", description = "Stewed beans on a bed of rice with choice of protein", food_trucks = truck2, price = 10)
        item6 = Menu_Item(item = "Tostones", description = "Count of 6 twice fried plantains", food_trucks = truck2, price = 10)
        #Food Truck 3
        item7 = Menu_Item(item = "Sabrett Hot-Dog", description = "Its a hot dog", food_trucks = truck3, price = 8)
        item8 = Menu_Item(item = "Russian Salad", description = "Mixed salad with boiled potatoes", food_trucks = truck3, price = 8)
        item9 = Menu_Item(item = "Lamb Kabob", description = "Lamb kabob on a skewer", food_trucks = truck3, price = 10)
        #create orders
        #orders for first truck
        ord1 = Order(order_number = 1, food_truck = truck1, customer = cust1)
        ord2 = Order(order_number = 2, food_truck = truck1, customer = cust2)
        ord3 = Order(order_number = 3, food_truck= truck1, customer = cust3)
        #orders for second truck
        ord4 = Order(order_number = 4, food_truck = truck2, customer = cust1)
        ord5 = Order(order_number = 5, food_truck = truck2, customer = cust2)
        ord6 = Order(order_number = 6, food_truck = truck2, customer = cust3)
        #orders for third truck
        ord7 = Order(order_number = 7, food_truck = truck3, customer = cust1)
        ord8 = Order(order_number = 8, food_truck = truck3, customer = cust2)
        ord9 = Order(order_number = 9, food_truck = truck3, customer = cust3)
        #create orders from the truck
        ticket1 = Menu_Order(order = ord1, menu_items = item1, quantity = 2)

       
        session.add_all([truck1, truck2, truck3, cust1, cust2, cust3, item1, item2, item3, 
                         item4, item5, item6, item7, item8, item9,ord1,ord2,
                         ord3,ord4,ord5,ord6,ord7,ord8,ord9,ticket1])
        
        session.commit()
      