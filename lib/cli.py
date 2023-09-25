from Models.classes import Food_Truck, Customer, Base, create_engine, create
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
    main()
    
    engine = create_engine('sqlite:///food_truck.db')
    Base.metadata.create_all(engine)