#This file is where you will use query to interact with the CLI
# from Models.classes import Food_Truck, Customer, Base, Session
# from sqlalchemy import create_engine
from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Food_Truck")
    print("1. Customer")


if __name__ == "__main__":
    user = input("Please enter a name: ")
    print(user)
   
#     engine = create_engine('sqlite:///food_truck.db')
#     # Food_Truck.__table__.drop(engine)
#     Base.metadata.create_all(engine)
    
#     with Session(engine) as session:
#         eazy_t = Food_Truck(name = "Eazy T's", food_type = "American Classics with Green Chili")
#         luisa = Food_Truck(name = "Luisa's", food_type = "Comida de Dominicana")
#         session.add_all([eazy_t, luisa])
#         session.commit()
#         # all_trucks = session.query(Food_Truck).all()
#         # print(all_trucks)
#         # one_truck = session.query(Food_Truck).filter(Food_Truck.id == 1).first()
#         # print(one_truck)
#         # session.delete(one_truck)

      
        
    