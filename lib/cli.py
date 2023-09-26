#This file is where you will use query to interact with the CLI
# from Models.classes import Food_Truck, Customer, Base, Session
# from sqlalchemy import create_engine
import inquirer
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
    user = input("Are you a Food Truck or a Customer?:")
    print(user)
    if user == "Customer" or user == 'customer':
        print("Press 1 to view the menu")
    if user == "Food Truck":
        print("Press 1 to view the menu")


      
        
    