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

def calculate_total(selected_items):
    """Calculate the total price of selected items."""
    total_price = 0
    for item, quantity in selected_items:
        total_price += item.price * quantity
    return total_price

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
            # ASCII art for Food Truck
                    print(r"""
             ________  ______    ______   _______         ________  _______   __    __   ______   __    __   ______  
            /        |/      \  /      \ /       \       /        |/       \ /  |  /  | /      \ /  |  /  | /      \ 
            $$$$$$$$//$$$$$$  |/$$$$$$  |$$$$$$$  |      $$$$$$$$/ $$$$$$$  |$$ |  $$ |/$$$$$$  |$$ | /$$/ /$$$$$$  |
            $$ |__   $$ |  $$ |$$ |  $$ |$$ |  $$ |         $$ |   $$ |__$$ |$$ |  $$ |$$ |  $$/ $$ |/$$/  $$ \__$$/ 
            $$    |  $$ |  $$ |$$ |  $$ |$$ |  $$ |         $$ |   $$    $$< $$ |  $$ |$$ |      $$  $$<   $$      \ 
            $$$$$/   $$ |  $$ |$$ |  $$ |$$ |  $$ |         $$ |   $$$$$$$  |$$ |  $$ |$$ |   __ $$$$$  \   $$$$$$  |
            $$ |     $$ \__$$ |$$ \__$$ |$$ |__$$ |         $$ |   $$ |  $$ |$$ \__$$ |$$ \__/  |$$ |$$  \ /  \__$$ |
            $$ |     $$    $$/ $$    $$/ $$    $$/          $$ |   $$ |  $$ |$$    $$/ $$    $$/ $$ | $$  |$$    $$/ 
            $$/       $$$$$$/   $$$$$$/  $$$$$$$/           $$/    $$/   $$/  $$$$$$/   $$$$$$/  $$/   $$/  $$$$$$/ 
                     """)

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
                        item_price = float(input("Enter the item price: "))  # Convert input to float

                     # Create a new menu item and associate it with the selected Food Truck
                        new_menu_item = Menu_Item(
                        item=item_name,
                        description=item_description,
                         price=item_price,
                        )
    
                    # Add the new menu item to the selected Food Truck's menu_items relationship
                        selected_food_truck.menu_items.append(new_menu_item)

                    # Add the new menu item to the session and commit the changes
                        session.add(new_menu_item)
                        session.commit()

                        print(f"Menu item '{item_name}' added to {selected_food_truck.name}'s menu.")

                    elif food_truck_action == "Update Menu Item":
                        # Display the menu items of the selected Food Truck
                        display_menu(selected_food_truck)

                        # Ask the user to select a menu item to update
                        menu_item_id = input("Enter the ID of the menu item you want to update: ")

                        # Check if the selected menu item exists for the selected food truck
                        selected_menu_item = (
                            session.query(Menu_Item)
                            .join(Food_Truck)
                            .filter(Menu_Item.id == menu_item_id, Food_Truck.id == selected_food_truck.id)
                            .first()
                        )

                        if selected_menu_item:
                            # Get the new details for the menu item from the user
                            new_item_name = input("Enter the new item name (leave empty to keep current): ")
                            new_item_description = input("Enter the new item description (leave empty to keep current): ")
                            new_item_price = input("Enter the new item price (leave empty to keep current): ")

                            # Update the selected menu item with the new details
                            if new_item_name:
                                selected_menu_item.item = new_item_name
                            if new_item_description:
                                selected_menu_item.description = new_item_description
                            if new_item_price:
                                selected_menu_item.price = float(new_item_price)

                            # Commit the changes to the database
                            session.commit()

                            print(f"Menu item {selected_menu_item.item} updated.")
                        else:
                            print("Invalid menu item ID. Please select a valid ID.")

                    # Inside the "if food_truck_action == 'Delete Menu Item':" block
                    elif food_truck_action == "Delete Menu Item":
                        # Display the menu items of the selected Food Truck
                        display_menu(selected_food_truck)

                        # Ask the user to select a menu item to delete
                        menu_item_id = input("Enter the ID of the menu item you want to delete: ")

                        # Check if the selected menu item exists for the selected food truck
                        selected_menu_item = (
                            session.query(Menu_Item)
                            .join(Food_Truck)
                            .filter(Menu_Item.id == menu_item_id, Food_Truck.id == selected_food_truck.id)
                            .first()
                        )

                        if selected_menu_item:
                            # Confirm the deletion with the user
                            confirm_deletion = input(f"Are you sure you want to delete '{selected_menu_item.item}'? (yes/no): ")
                            
                            if confirm_deletion.lower() == "yes":
                                # Delete the selected menu item
                                session.delete(selected_menu_item)
                                session.commit()

                                print(f"Menu item '{selected_menu_item.item}' deleted.")
                            else:
                                print(f"Menu item '{selected_menu_item.item}' was not deleted.")
                        else:
                            print("Invalid menu item ID. Please select a valid ID.")


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


            print(r""" 
                ______   ____  ____   ________  ___________  ______   ___      ___   _______   _______   
                /" _  "\ ("  _||_ " | /"       )("     _   ")/    " \ |"  \    /"  | /"     "| /"      \  
                (: ( \___)|   (  ) : |(:   \___/  )__/  \\__/// ____  \ \   \  //   |(: ______)|:        | 
                \/ \     (:  |  | . ) \___  \       \\_ /  /  /    ) :)/\\  \/.    | \/    |  |_____/   ) 
                //  \ _   \\ \__/ //   __/  \\      |.  | (: (____/ //|: \.        | // ___)_  //      /  
                (:   _) \  /\\ __ //\  /" \   :)     \:  |  \        / |.  \    /:  |(:      "||:  __   \  
                \_______)(__________)(_______/       \__|   \"_____/  |___|\__/|___| \_______)|__|  \___) 

            """)
            # Get the customer's name
            customer_name = input("Enter your name: ")
            print(f"Hello, {customer_name}!")

            # Create a new session for the customer
            session = Session()

            # Display the list of available Food Trucks
            display_food_trucks(session)

            # Ask the customer to select a Food Truck
            food_truck_id = input("Enter the ID of the Food Truck you want to order from: ")
            selected_food_truck = session.query(Food_Truck).filter_by(id=food_truck_id).first()

            if selected_food_truck:
                # Handle the case when a Customer is selected
                # You can add options for a Customer here, such as viewing menu items or placing orders
                pass
            else:
                print("Invalid Food Truck ID. Please select a valid ID.")

            session.close()  # Close the customer's session when done

        elif choice == "Exit":
            break

        else:
            print("Invalid choice")

    print("Goodluck, Chef!")






# from Models.classes import Food_Truck, Customer, Order, Menu_Item, Menu_Order, Base
# import inquirer
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # Create a database connection
# engine = create_engine("sqlite:///food_truck.db")
# Session = sessionmaker(bind=engine)

# def display_food_trucks(session):
#     """Display the list of available Food Trucks."""
#     print("Available Food Trucks:")
#     for truck in session.query(Food_Truck).all():
#         print(f"{truck.id}. {truck.name} - Cuisine: {truck.food_type}")

# def display_menu(food_truck):
#     print(f"Menu for {food_truck.name}:")
#     for item in food_truck.menu_items:
#         print(f"{item.id}. {item.item} - {item.description} - Price: ${item.price}")

# if __name__ == "__main__":
#     # Create a session outside of the loop
#     session = Session()

#     while True:
#         # Ask the user to choose between Food Truck and Customer
#         questions = [
#             inquirer.List(
#                 name="user_type",
#                 message="Welcome, Are you a Food Truck or Customer?",
#                 choices=["Food Truck", "Customer", "Exit"],
#             ),
#         ]

#         answers = inquirer.prompt(questions)

#         choice = answers["user_type"]

#         if choice == "Food Truck":
#             # ASCII art for Food Truck
#             print(r"""
#                  ________  ______    ______   _______         ________  _______   __    __   ______   __    __   ______  
#                 /        |/      \  /      \ /       \       /        |/       \ /  |  /  | /      \ /  |  /  | /      \ 
#                 $$$$$$$$//$$$$$$  |/$$$$$$  |$$$$$$$  |      $$$$$$$$/ $$$$$$$  |$$ |  $$ |/$$$$$$  |$$ | /$$/ /$$$$$$  |
#                 $$ |__   $$ |  $$ |$$ |  $$ |$$ |  $$ |         $$ |   $$ |__$$ |$$ |  $$ |$$ |  $$/ $$ |/$$/  $$ \__$$/ 
#                 $$    |  $$ |  $$ |$$ |  $$ |$$ |  $$ |         $$ |   $$    $$< $$ |  $$ |$$ |      $$  $$<   $$      \ 
#                 $$$$$/   $$ |  $$ |$$ |  $$ |$$ |  $$ |         $$ |   $$$$$$$  |$$ |  $$ |$$ |   __ $$$$$  \   $$$$$$  |
#                 $$ |     $$ \__$$ |$$ \__$$ |$$ |__$$ |         $$ |   $$ |  $$ |$$ \__$$ |$$ \__/  |$$ |$$  \ /  \__$$ |
#                 $$ |     $$    $$/ $$    $$/ $$    $$/          $$ |   $$ |  $$ |$$    $$/ $$    $$/ $$ | $$  |$$    $$/ 
#                 $$/       $$$$$$/   $$$$$$/  $$$$$$$/           $$/    $$/   $$/  $$$$$$/   $$$$$$/  $$/   $$/  $$$$$$/ 
#                          """)

#             # Rest of the Food Truck branch of the code
#             while True:
#                 food_truck_actions = [
#                     inquirer.List(
#                         name="food_truck_action",
#                         message="Choose a Food Truck action:",
#                         choices=["Add Menu Item", "Update Menu Item", "Delete Menu Item", "View Menu", "Back"],
#                     ),
#                 ]
#                 food_truck_answers = inquirer.prompt(food_truck_actions)
#                 food_truck_action = food_truck_answers["food_truck_action"]

#                 if food_truck_action == "Add Menu Item":
#                     # Code to add a new menu item for the selected Food Truck
#                     item_name = input("Enter the item name: ")
#                     item_description = input("Enter the item description: ")
#                     item_price = float(input("Enter the item price: "))  # Convert input to float

#                     # Create a new menu item and associate it with the selected Food Truck
#                     new_menu_item = Menu_Item(
#                         item=item_name,
#                         description=item_description,
#                         price=item_price,
#                         food_truck_id=selected_food_truck.id
#                     )

#                     # Add the new menu item to the selected Food Truck's menu_items relationship
#                     selected_food_truck.menu_items.append(new_menu_item)

#                     # Add the new menu item to the session and commit the changes
#                     session.add(new_menu_item)
#                     session.commit()

#                     print(f"Menu item '{item_name}' added to {selected_food_truck.name}'s menu.")

#                 elif food_truck_action == "Update Menu Item":
#                     # Display the menu items of the selected Food Truck
#                     display_menu(selected_food_truck)

#                     # Ask the user to select a menu item to update
#                     menu_item_id = input("Enter the ID of the menu item you want to update: ")

#                     # Check if the selected menu item exists for the selected food truck
#                     selected_menu_item = (
#                         session.query(Menu_Item)
#                         .join(Food_Truck)
#                         .filter(Menu_Item.id == menu_item_id, Food_Truck.id == selected_food_truck.id)
#                         .first()
#                     )

#                     if selected_menu_item:
#                         # Get the new details for the menu item from the user
#                         new_item_name = input("Enter the new item name (leave empty to keep current): ")
#                         new_item_description = input("Enter the new item description (leave empty to keep current): ")
#                         new_item_price = input("Enter the new item price (leave empty to keep current): ")

#                         # Update the selected menu item with the new details
#                         if new_item_name:
#                             selected_menu_item.item = new_item_name
#                         if new_item_description:
#                             selected_menu_item.description = new_item_description
#                         if new_item_price:
#                             selected_menu_item.price = float(new_item_price)

#                         # Commit the changes to the database
#                         session.commit()

#                         print(f"Menu item {selected_menu_item.item} updated.")
#                     else:
#                         print("Invalid menu item ID. Please select a valid ID.")

#                 elif food_truck_action == "Delete Menu Item":
#                     # Display the menu items of the selected Food Truck
#                     display_menu(selected_food_truck)

#                     # Ask the user to select a menu item to delete
#                     menu_item_id = input("Enter the ID of the menu item you want to delete: ")

#                     # Check if the selected menu item exists for the selected food truck
#                     selected_menu_item = (
#                         session.query(Menu_Item)
#                         .join(Food_Truck)
#                         .filter(Menu_Item.id == menu_item_id, Food_Truck.id == selected_food_truck.id)
#                         .first()
#                     )

#                     if selected_menu_item:
#                         # Confirm the deletion with the user
#                         confirm_deletion = input(f"Are you sure you want to delete '{selected_menu_item.item}'? (yes/no): ")

#                         if confirm_deletion.lower() == "yes":
#                             # Delete the selected menu item
#                             session.delete(selected_menu_item)
#                             session.commit()

#                             print(f"Menu item '{selected_menu_item.item}' deleted.")
#                         else:
#                             print(f"Menu item '{selected_menu_item.item}' was not deleted.")
#                     else:
#                         print("Invalid menu item ID. Please select a valid ID.")

#                 elif food_truck_action == "View Menu":
#                     # Display the menu items for the selected Food Truck
#                     display_menu(selected_food_truck)
#                     input("Press Enter to continue...")

#                 elif food_truck_action == "Back":
#                     session.close()
#                     break

#                 else:
#                     print("Invalid Food Truck action")

#         elif choice == "Customer":

#             if choice == "Customer":
#             # ASCII art for Food Truck
#                 print(r"""
#                     ______   ____  ____   ________  ___________  ______   ___      ___   _______   _______   
#                     /" _  "\ ("  _||_ " | /"       )("     _   ")/    " \ |"  \    /"  | /"     "| /"      \  
#                     (: ( \___)|   (  ) : |(:   \___/  )__/  \\__/// ____  \ \   \  //   |(: ______)|:        | 
#                     \/ \     (:  |  | . ) \___  \       \\_ /  /  /    ) :)/\\  \/.    | \/    |  |_____/   ) 
#                     //  \ _   \\ \__/ //   __/  \\      |.  | (: (____/ //|: \.        | // ___)_  //      /  
#                     (:   _) \  /\\ __ //\  /" \   :)     \:  |  \        / |.  \    /:  |(:      "||:  __   \  
#                     \_______)(__________)(_______/       \__|   \"_____/  |___|\__/|___| \_______)|__|  \___) 
#                  """)


#             # Handle the case when a Customer is selected
#             customer_name = input("Enter your name: ")
#             print(f"Hello, {customer_name}!")

#             while True:
#                 display_food_trucks(session)

#                 food_truck_choice = input("Enter the ID of the Food Truck you want to order from (or 'exit' to go back): ")

#                 if food_truck_choice.lower() == 'exit':
#                     break

#                 selected_food_truck = session.query(Food_Truck).filter_by(id=food_truck_choice).first()

#                 if selected_food_truck:
#                     display_menu(selected_food_truck)
#                     customer_order = Order(customer_name=customer_name, food_truck=selected_food_truck)

#                     while True:
#                         item_choice = input("Enter the ID of the menu item you want to order (or 'done' to finish): ")

#                         if item_choice.lower() == 'done':
#                             break

#                         selected_item = session.query(Menu_Item).filter_by(id=item_choice).first()

#                         if selected_item:
#                             quantity = int(input(f"How many '{selected_item.item}' do you want to order? "))
#                             menu_order = Menu_Order(menu_item=selected_item, quantity=quantity)
#                             customer_order.menu_items.append(menu_order)
#                             session.commit()
#                             print(f"{quantity} '{selected_item.item}' added to your order.")
#                         else:
#                             print("Invalid menu item ID. Please select a valid ID.")

#                     total_price = sum(menu_order.menu_item.price * menu_order.quantity for menu_order in customer_order.menu_items)
#                     print(f"Total price for your order from {selected_food_truck.name}: ${total_price:.2f}")

#                 else:
#                     print("Invalid Food Truck ID. Please select a valid ID.")

#         elif choice == "Exit":
#             session.close()  # Close the session when exiting
#             break

#         else:
#             print("Invalid choice")

#     print("Goodbye!")
