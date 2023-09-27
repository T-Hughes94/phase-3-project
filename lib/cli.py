from Models.classes import Food_Truck, Customer, Order, Menu_Item, Menu_Order, Base
import inquirer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a database connection
engine = create_engine("sqlite:///food_truck.db")
Session = sessionmaker(bind=engine)

def display_food_trucks(session):
    """Display the list of available Food Trucks."""
    print("Available Food Trucks:")
    for truck in session.query(Food_Truck).all():
        print(f"{truck.id}. {truck.name} - Cuisine: {truck.food_type}")

def display_menu(food_truck):
    print(f"Menu for {food_truck.name}:")
    for item in food_truck.menu_items:
        print(f"{item.id}. {item.item} - {item.description} - Price: ${item.price}")

if __name__ == "__main__":
    while True:
        # Ask the user to choose between Food Truck and Customer
        questions = [
            inquirer.List(
                name="user_type",
                message="Welcome, Are you a Food Truck or Customer?",
                choices=["Food Truck", "Customer", "Exit"],
            ),
        ]

        answers = inquirer.prompt(questions)

        choice = answers["user_type"]

        if choice == "Food Truck":
            # Create a new session for this branch of the code
            session = Session()
            
            # Display the list of available Food Trucks
            display_food_trucks(session)

            # Ask the user to select a Food Truck
            food_truck_id = input("Enter the ID of the Food Truck you want to manage: ")
            selected_food_truck = session.query(Food_Truck).filter_by(id=food_truck_id).first()

            if selected_food_truck:
                # Handle the case when a Food Truck is selected
                food_truck_actions = [
                    inquirer.List(
                        name="food_truck_action",
                        message="Choose a Food Truck action:",
                        choices=["Add Menu Item", "Update Menu Item", "Delete Menu Item", "View Menu", "Back"],
                    ),
                ]
                while True:
                    food_truck_answers = inquirer.prompt(food_truck_actions)
                    food_truck_action = food_truck_answers["food_truck_action"]

                    if food_truck_action == "Add Menu Item":
                        # Code to add a new menu item for the selected Food Truck
                        item_name = input("Enter the item name: ")
                        item_description = input("Enter the item description: ")
                        item_price = float(input("Enter the item price: "))

                        new_menu_item = Menu_Item(
                        item = item_name,
                        description = item_description,
                        price = item_price,
                        food_truck = selected_food_truck,
                        )

                        selected_food_truck.menu_items.append(new_menu_item)

                        session.add(new_menu_item)
                        session.commit()

                        print(f"Menu item '{item_name}' added to {selected_food_truck.name}'s menu.")

                    elif food_truck_action == "Update Menu Item":
                        pass
                        # Code to update an existing menu item for the selected Food Truck
                        # ...

                    elif food_truck_action == "Delete Menu Item":
                        pass
                        # Code to delete an existing menu item for the selected Food Truck
                        # ...

                    elif food_truck_action == "View Menu":
                        # Display the menu items for the selected Food Truck
                        display_menu(selected_food_truck)
                        input("Press Enter to continue...")

                    elif food_truck_action == "Back":
                        session.close()
                        break

                    else:
                        print("Invalid Food Truck action")
            else:
                print("Invalid Food Truck ID. Please select a valid ID.")

        elif choice == "Customer":
            # Handle the case when a Customer is selected
            # You can add options for a Customer here, such as viewing menu items or placing orders
            pass

        elif choice == "Exit":
            break

        else:
            print("Invalid choice")

    print("Goodbye!")











        
    