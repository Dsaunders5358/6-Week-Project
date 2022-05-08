#region import Block
import data
import csv
#endregion
#region Function_Block
def print_stars(length): # Formatting Line Break
    print("")
def get_main_menu(): # First screen user will see when terminal is accessed.
    print_stars()
    print("Main Menu")
    print_stars()
    print("Choose a number to pick an option. Type exit or 0 at any point to exit to previous menu")
    print("1) Products 2) Couriers 3) Orders 0) Exit")
    n = input("Option: ")
    if n == "0" or n.lower() == "exit":
        print_stars()
        print("Goodbye")
        data.save_data(product_list, "product_list.txt")
        data.save_data(courier_list, "courier_list.txt")
    elif n == "1" or n.lower() == "product":
        get_list_menu("product")
    elif n == "2" or n.lower() == "courier":
        get_list_menu("courier")
    elif n == "3" or n.lower() == "courier":
        get_orders_menu()
    else:
        print("Sorry, I don't recognise that command. Type help to show a list of available commands")
        get_main_menu()
def get_list_menu(type):  #Top menu for Specific Lists
    print_stars()
    print(f"{type} Menu")
    print_stars()
    print(f"1) Show Current {type} 2) Add New {type} 3) Change Existing {type}s 4) Delete Existing {type}s 0) Exit Menu")
    x = input("Option: ")
    if x == "0" or x.lower() == "exit":
        print("Exiting to Main Menu")
        get_main_menu()
    elif x == "1":
        print_list(type)
        input("Press Enter to Continue")
        get_list_menu(type)
    elif x == "2":
        get_add_menu(type)
    elif x == "3":
        change_list_item(type)
    elif x == "4":
        delete_list_item(type)
    else:
        print("Invalid Entry. Returning to menu")
        get_list_menu(type)
def get_add_menu(type):  #Menu for adding to list
    print_stars()
    print(f"What {type} would you like to add?")
    print_stars()
    name = input(f"{type}: ")
    if name == "0" or name.lower() == "exit":
        print("Exiting to previous menu")
        get_list_menu(type)
    else:
        add_list_item(type, name)
def add_list_item(type, name): # adding item to list functionality
    list_item = name.title()
    print(f"Confirm you wish to add {list_item} to {type} database (Y or N)")
    confirm = input("Confirm: ")
    if confirm.lower() == "y":
        if type.lower() == "product":
            global product_list
            product_list.append(list_item.strip())
        elif type.lower() == "courier":
            global courier_list
            courier_list.append(list_item.strip())
        print(f"{list_item} added to database")
        get_add_menu(type)
    else:
        print("Returning to menu")
        get_add_menu(type)
def print_list(type):  #prints list with index added
    list_type = []
    if type == "product":
        list_type = product_list
    elif type == "courier":
        list_type = courier_list
    elif type == "order":
        list_type = order_list
    if len(list_type) > 0:
        for counter, value in enumerate(list_type, 1):
            print(counter, value)
    else:
        print(f"No {type} in database")
def change_list_item(type): #Change Specific value in list based on index
    print_stars()
    print(f"Changing {type}")
    print_stars()
    print_list(type)
    print("Choose number you would like to change from list. 0 to exit")
    num = input("Number: ")
    if type == "product":
        global product_list
        change_list = product_list
    elif type == "courier":
        global courier_list
        change_list = courier_list
    if num == "0" or num.lower() == "exit":
        get_list_menu(type)
    elif int(num) - 1 <= len(change_list) and int(num) > 0:
        print("{} chosen, type new name to change it to".format(change_list[int(num) - 1]))
        new_name = input("Name: ")
        print("Confirm you wish to change {} to {} (Y or N)".format(change_list[int(num) - 1], new_name))
        confirm = input("Confirm: ")
        if confirm == "y":
            change_list[int(num) - 1] = new_name.title()
            if type == "product":
                product_list = change_list
            elif type == "courier":
                courier_list = change_list
            print("Change Complete")
            change_list_item(type)
        else:
            print("Returning to menu")
            change_list_item(type)
def delete_list_item(type):  #deletes specific item oon list based on index
    print_stars()
    print(f"Deleting {type}")
    print_stars()
    print_list(type)
    print("Choose number you would like to delete from list. 0 to exit")
    num = input("Number: ")
    if type == "product":
        global product_list
        delete_list = product_list
    elif type == "courier":
        global courier_list
        delete_list = courier_list
    if num == "0" or num.lower() == "exit":
        get_list_menu(type)
    elif int(num) - 1 <= len(delete_list) and int(num) > 0:
        print("Confirm you wish to delete {} (Y or N)".format(delete_list[int(num) - 1]))
        confirm = input("Confirm: ")
        if confirm == "y":
            delete_list.pop(int(num) - 1)
            if type == "product":
                product_list = delete_list
            elif type == "courier":
                courier_list = delete_list
            print("Deleted")
            delete_list_item(type)
        else:
            print("Returning to menu")
            delete_list_item(type)
def get_orders_menu():
    print_stars()
    print(f"Orders Menu")
    print_stars()
    print("1) Show current orders 2) Add new order 3) Update Order Status 4) Change order Details 5) Remove Order's courier 0) Exit menu")
    x = input("Option: ")
    if x == "0" or x.lower() == "exit":
        print("Exiting to Main Menu")
        get_main_menu()
    elif x == "1":
        print("Current orders")
        print_list("order")
        input("Press 'Enter' key to continue")
        get_orders_menu()
    elif x == "2":
        get_add_orders_menu()
    elif x == "3":
        update_order_status()
    elif x == "4":
        change_order_menu()
    elif x == "5":
        delete_order_courier()
    else:
        print("Invalid Entry. Returning to menu")
        get_orders_menu()
def get_add_orders_menu():
    print_stars()
    print("Add New Order")
    print_stars()
    print("Please enter customer's name")
    name = input("Name: ")
    print("Please enter customers address")
    address = input("Address: ")
    print("Please enter customers telephone number")
    number = input("Number: ")
    print_list("courier")
    print("Please pick a courier to add by index number")
    courier_index = input("Index: ")
    add_new_order(name, address, number, courier_index)
def add_new_order(name, address, number, index):  #functionality for adding order to list
    order = {
        "customer_name" : name, 
        "customer_address" : address, 
        "customer_phone" : number,
        "courier" : courier_list[int(index)-1],
        "status" : "preparing"
    }
    print(order)
    print("Confirm new order? (Y or N)")
    confirm = input("Confirm: ")
    if confirm == "y":
        global order_list
        order_list.append(order)
    get_orders_menu()
def update_order_status():
    global order_list
    print_stars()
    print("Updating status of order")
    print_stars()
    print_list("order")
    print("Please choose index number of order to update")
    index = input("Index: ")
    try:
        if index == "0" or index.lower() == exit:
            print("Exiting Menu")
            get_orders_menu()
        elif int(index) > 0 and int(index) <= len(order_list):
            print("What do you want status to be updated to?")
            new_status = input("Status: ")
            print("Confirm you wish to update {} to {} (Y or N)".format(order_list[int(index) - 1]["status"], new_status))
            confirm = input("Confirm: ")
            if confirm.lower() == "y":
                order_list[int(index) - 1]["status"] = new_status
                print("Status Changed")
            else:
                print("Returning to Menu")
            update_order_status()
        else:
            print("Invalid index. returning to menu")
            update_order_status()
    except:
        print("Command not recognised. Returning to menu")
        update_order_status()
def change_order_menu():
    print_stars()
    print("Changing Order Details")
    print_stars()
    print_list("order")
    print("Which order number would you like to change the details of")
    index = input("Index: ")
    try:
        if index == "0" or index.lower() == "exit":
            print("Exiting Menu")
            get_orders_menu()
        elif int(index) > 0 and int(index) <= len(order_list):
            print(order_list)
            change_order_details(index)
    except:
        print("Invalid Command Entered, Returning to menu")
        change_order_menu()
def change_order_details(index):  #Iterates through orders, changing to input if not blank
    global order_list
    print("Going through each field 1 by 1. Leave blank to not change field")
    for keys in order_list[int(index) - 1]:
        new_value = input(keys + ": ")
        if len(new_value) > 0:
            order_list[int(index) - 1][keys] = new_value
        else:
            print(f"No Change for {keys}")
    print(order_list[int(index) - 1])
    print("Changed Order to the above")
    change_order_menu()
def delete_order_courier():  #delete order based on index
    print_stars()
    print("Remove Courier from Order")
    print_stars()
    print_list("order")
    print("Choose which order number you wish the remove the courier for")
    try:
        index = input("Order: ")
        global order_list
        if index == "0" or index.lower() == "exit":
            print("Returning to menu")
            get_orders_menu()
        elif int(index) > 0 and int(index) <= len(order_list):
            print(order_list[int(index) - 1])
            print("Confirm you wish to remove courier from above order? (Y or N)")
            confirm = input("Confirm: ")
            if confirm == "y":
                order_list[int(index) - 1]["courier"] = ""
                print("Courier has been removed")
            else:
                print("Returning to Menu")
            delete_order_courier()
    except:
        print("Invalid Index detected, Returning to menu")
        delete_order_courier()
#endregion
#region Variable_Block
product_list = data.load_data("product")
courier_list = data.load_data("courier")
order_list = []
order_list.append( {
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2,
"status": "preparing"
})
#endregion
try:
    get_main_menu()
except:
    data.save_data(product_list, "product_list.txt")
    data.save_data(courier_list, "courier_list.txt")
    print("An error has occured. Exiting Program")

def show_main_menu():
    print("Main Menu")
