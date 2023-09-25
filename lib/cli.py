from Models.classes import Food_Truck, Customer, Base, Session
from sqlalchemy import create_engine
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
    engine = create_engine('sqlite:///food_truck.db')
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        eazy_t = Food_Truck(name = "Eazy T's", food_type = "American Classics with Green Chili")
        session.add(eazy_t)
        session.commit()
        
    