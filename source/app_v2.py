#region Function Blocks
def program_start():
    menu = show_main_menu()
    while menu != "exit":
        menu = move_to_menu(menu)
    print("Exiting App\nGoodbye")
def generate_menu_options(*options):
    index = 1
    for option in options:
        print(f"{index}) {option}")
        index += 1
    print("0) Exit")
def print_title_stars(title):  #Formatting stars via title
    stars = ""
    for char in range(0, len(title)):
        stars += "*"
    print(stars)
    print(title)
    print(stars)
def show_main_menu():  # First menu user will see
    print_title_stars("Main Menu")
    print("Please Choose a Menu Option.\n1) Products\n2) Couriers\n3) Orders\n0) Exit Program")
    nav = input("Option: ")
    if nav == "1":
        return "products main"
    elif nav == "2":
        return "couriers main"
    elif nav == "3":
        return "orders main"
    elif nav == "0":
        return "exit"
def move_to_menu(menu):  # For each string returned, move to a differet menu
    if menu == "main menu":
        return show_main_menu()
    elif menu == "products main":
        return show_type_main_menu("product")
    elif menu == "products add":
        return show_product_add_menu()
    elif menu == "products remove":
        return show_product_del_menu()
    elif menu == "products update":
        return show_product_update_menu()
    elif menu == "couriers main":
        return show_type_main_menu("courier")
    elif menu == "couriers add":
        return show_courier_add_menu()
    elif menu == "couriers remove":
        return show_courier_del_menu()
    elif menu == "couriers update":
        return show_courier_update_menu()
    elif menu == "orders main":
        return show_orders_main_menu()
    elif menu == "orders add":
        return show_orders_add_menu()
    elif menu == "orders status":
        return show_orders_status_menu()
    elif menu == "orders update":
        return show_orders_update_menu()
    elif menu == "orders del courier":
        return show_orders_del_courier_menu()
def show_type_main_menu(type):
    print_title_stars("{} menu".format(type.title())) 
    generate_menu_options(f"Show current {type}s",f"Add new {type}" , f"Update Existing {type}s", f"Delete a {type}")
    print("Please choose an option")
    nav = input("Option: ")
    if nav == "1":
        pass # Print Lists goes here
    elif nav == "2":
        return f"{type}s add"
    elif nav == "3":
        return f"{type}s update"
    elif nav == "4":
        return f"{type}s remove"
    elif nav == "0":
        return "main menu"
    else:
        print("Option not available. Please choose another option.")
        return f"{type}s main"
def show_product_add_menu():
    print_title_stars("Add New Product Menu")
    print("Please input name of product you wish to add")
    name = input("Name: ").title()
    print("Please input price of {} (Without £ symbol)".format(name))
    price = input("Price: ")
    # Run function here which takes name and price adds them to dictionary and appends them to a list of dictionaries
    print(f"{name} successfully added. Returning to Products Menu")
    return "products main"
def show_product_del_menu():
    print_title_stars("Delete a Product")
    #insert function here which prints a list of keys from the product dictionary
    print("Type index of product you wish to delete. 0 will exit")
    index = input("Option: ")
    #insert function which will remove an item from a dictionary
    print("Product removed successfully. Returning to products menu")
    return "products main"
def show_product_update_menu():
    print_title_stars("Update a product")
    #insert function here which prints a list of keys from the product dictionary
    print("Type index of product you wish to change. 0 will exit")
    index = input("Option: ")
    #insert function which will go through the key and value pair of selected index and update it accordingly
    print("Product Updated. Returning to products menu")
    return "products main"
def show_courier_add_menu():
    print_title_stars("Add new courier menu")
    print("Please input name of courier you would like to add. type 0 to exit")
    name = input("Name: ").title()
    print(f"Please input phone number for {name}")
    num = input("Number: ")
    #insert function here for adding name and number to a courier and adding to list of courier dictionaries
    print(f"{name} added to database. Returning to courier menu")
    return "couriers main"
def show_courier_del_menu():
    print_title_stars("Delete a courier")
    # Insert function here which shows a list of current dictonaries in courier with their index number
    print("Type index of courier you wish to delete. 0 will exit")
    index = input("Index: ")
    # Insert function here which will remove courier from list of dictionaries
    print("Courier deleted successfully. Returning to courier menu.")
    return "couriers main"
def show_courier_update_menu():
    print_title_stars("Update a Courier")
    #insert function to print an enumerated list of couriers dictionaries
    print("Type index of courier you wish to change. 0 to exit")
    index = input("Option: ")
    #insert function which will go through the key and value pair of selected index and update it accordingly
    print("Courier Updated. Returning to courier menu")
    return "couriers main"
def show_orders_main_menu():
    print_title_stars("Orders Main Menu")
    generate_menu_options("Show Existing Orders", "Add new order", "Update order status", "Update order details", "Delete Courier from Order")
    print("Please choose an option")
    nav = input("Option: ")
    if nav == "1":
        pass #insert function for printing product list here
    elif nav == "2":
        return "orders add"
    elif nav == "3":
        return "orders status"
    elif nav == "4":
        return "orders update"
    elif nav == "5":
        return "orders del courier"
    elif nav == "0":
        return "main menu"
    else:
        print("Invalid option. Please enter a valid number.")
        return "orders main"
def show_orders_add_menu():
    print_title_stars("Add New Order Menu")
    print("Entering details for a new order. Type 0 in any field to cancel and exit to main orders menu")
    print("Please enter customers name")
    name = input("Name: ")
    if name =="0":
        print("Cancelling order. returning to orders menu")
        return "orders main"
    print("Please enter customers address")
    address = input("Address: ")
    if address =="0":
        print("Cancelling order. returning to orders menu")
        return "orders main"
    print("Please enter customer's phone number")
    number = input("Number: ")
    if number =="0":
        print("Cancelling order. returning to orders menu")
        return "orders main"
    #enter function here which takes the name address and number and add them to dictionary while asking user to input products they want to add to order
    print (f"Order for customer {name} has been added. Returning to orders menu")
    return ("orders main")
def show_orders_status_menu():
    print_title_stars("Update Order Status")
    #Insert function here which shows list of orders with index value
    print("Type index of order you would to update the status of. Type 0 to exit to orders menu")
    index = input("Order: ")
    if index == "0":
        print("Cancelling change, returning to orders menu")
        return ("orders main")
    #insert function which updates the status of order here
    print("order status changed successfully. Returning to orders menu")
    return "orders main" 
def show_orders_update_menu():
    print_title_stars("Updating Order Details")
    #print a list of orders
    print("Which order would you like to update the details of. Type 0 to exit")
    index = input("Order: ")
    if index =="0":
        print("Cancelling change. Returning to orders menu")
        return "orders main"
    #takes to function which changes the details of the order
    print("Order details changed successfully")
    return "orders main"
def show_orders_del_courier_menu():
    print_title_stars("Delete Courier from Order")
    # show a list of orders
    print("Type index of order you would like to remove courier from. Type 0 to exit")
    index = input("Order: ")
    if index == "0":
        print("Cancelling action. Returning to orders menu")
        return "orders main"
    #run function to remove courier from index
    print("Courier successfully removed from order")
    return "orders main"
#endregion
program_start()