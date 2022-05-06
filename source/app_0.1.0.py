#region import Block
import data
#endregion
#region Function_Block
def menu_stars(): # Line that Underlines options for readability
    print("***********************************")
def print_products(): # Prints products in the list with index values
    global product_list
    if len(product_list) > 0:
        for i in range(0, len(product_list)):
            print(str(i + 1) + ") " + product_list[i])
    else:
        print("No products available")
def sort_products(): #Sorts product list alphabetically and removes any duplicates
    global product_list
    product_list = sorted(list(set(product_list)))
def main_menu(): # First screen user will see when terminal is accessed.
    menu_stars()
    print("Main Menu")
    menu_stars()
    print("Choose a number to pick an option. Type exit or 0 at any point to exit to previous menu")
    print("1) Products 2) Couriers 0) Exit")
    n = input("Option: ")
    if n == "0" or n.lower() == "exit":
        menu_stars()
        print("Goodbye")
        global product_list
        data.product_data_save(product_list)
        data.courier_data_save(courier_list)
    elif n == "1" or n.lower() == "products":
        product_menu()
    elif n == "2" or n.lower() == "couriers":
        courier_menu()
    else:
        print("Sorry, I don't recognise that command. Type help to show a list of available commands")
        main_menu()
def product_menu(): #Menu for selecting what to do with different products
    menu_stars()
    print("Product Menu")
    menu_stars()
    print("1) Show Current Products 2) Add New Product 3) Change Existing Product 4) Delete Existing Product 0) Exit Menu")
    x = input("Option: ")
    if x == "0" or x.lower() == "exit":
        print("Exiting to Main Menu")
        main_menu()
    elif x == "1" or x.lower == "show products" or x.lower == "show current products":
        global product_list
        print("Current Products")
        if len(product_list) > 0:
            print(product_list)
        else:
            print("Product List is empty")
        input("Press Enter to Continue")
        product_menu()
    elif x == "2":
        add_product_menu()
    elif x == "3":
        change_product()
    elif x == "4":
        delete_product()
    else:
        print("Invalid Entry. Returning to menu")
        product_menu()
def add_product_menu(): #Take user to menu to add a product to the product list variable
    menu_stars()
    print("What product would you like to add?")
    menu_stars()
    x = input("Product: ")
    if x == "0" or x.lower() == "exit":
        print("Exiting to Product Menu")
        product_menu()
    else:
        add_product_input(x)
def add_product_input(product): #The code for adding a code to the product list
    menu_stars()
    global product_list
    #Takes a list enforces title formatting, removes additional whitespace adds to product list and sorts them alphabetically while removing direct dupicates
    product = product.title()
    product_list.append(product.strip())
    sort_products()
    print(f"Product {product} added to database")
    print("Would you like to add another product? Type 0 to exit or input name of new product")
    x = input("Product: ")
    if x == "0" or x =="exit":
        product_menu()
    else:
        add_product_input(x)
def change_product(): # Changes a product on the list to a new variable specified by user
    global product_list
    menu_stars()
    print("Product Names with Numbers")
    menu_stars()
    sort_products()
    print_products()
    print("Which product number would you like to change?")
    n = input("Product name: ")
    if n == "0" or n.lower() == "exit":
        product_menu()
    elif int(n) - 1 <= len(product_list):
        print("What would you like to change it to?")
        x = input("New Name: ")
        product_list[int(n)-1] = x
        change_product()
    else:
        print("Sorry, I don't recognise that command. Type help to show a list of available commands")
        change_product()
def delete_product(): # Prints product list and deletes an item from the list based on index 
    global product_list
    menu_stars()
    print("Delete a Product from List")
    menu_stars()
    print_products()
    print("Which product would you like to delete?")
    x = input("Product Number: ")
    if x == "0" or x == "exit":
        product_menu()
    elif int(x) - 1 < len(product_list) and int(x) > 0:
        print("Confirm you wish to delete {}? (Y or N)".format(product_list[int(x)-1])) #Confirmation to delete otherwise return to top of menu
        n = input("Confirm?: ")
        if n.lower() == "y":
            product_list.pop(int(x) - 1)
            delete_product()
        elif n.lower() == "n":
            delete_product()
        else:
            print("Invalid Entry. Returning to Menu")
            delete_product()
def add_courier_input(courier): #The code for adding a code to the courier list
    menu_stars()
    global courier_list
    #Takes a list enforces title formatting, removes additional whitespace adds to product list and sorts them alphabetically while removing direct dupicates
    courier = courier.title()
    courier_list.append(courier.strip())
    sort_couriers()
    print(f"Courier {courier} added to database")
    print("Would you like to add another courier? Type 0 to exit or input name of new courier")
    x = input("Courier: ")
    if x == "0" or x =="exit":
        courier_menu()
    else:
        add_courier_input(x)
def print_couriers(): # Prints couriers in the list with index values
    global courier_list
    if len(courier_list) > 0:
        for i in range(0, len(courier_list)):
            print(str(i + 1) + ") " + courier_list[i])
    else:
        print("No couriers available")
def sort_couriers(): #Sorts Courier list alphabetically and removes any duplicates
    global courier_list
    courier_list = sorted(list(set(courier_list)))
def courier_menu(): #Menu for selecting what to do with different couriers
    menu_stars()
    print("Courier Menu")
    menu_stars()
    print("1) Show Current Couriers 2) Add New Courier 3) Change Existing Courier 4) Delete Existing Courier 0) Exit Menu")
    x = input("Option: ")
    if x == "0" or x.lower() == "exit":
        print("Exiting to Main Menu")
        main_menu()
    elif x == "1" or x.lower == "show couriers" or x.lower == "show current couriers":
        global courier_list
        print("Current Couriers")
        if len(courier_list) > 0:
            print(courier_list)
        else:
            print("Courier List is empty")
        input("Press Enter to Continue")
        courier_menu()
    elif x == "2":
        add_courier_menu()
    elif x == "3":
        change_courier()
    elif x == "4":
        delete_courier()
    else:
        print("Invalid Entry. Returning to menu")
        courier_menu()
def add_courier_menu(): #Take user to menu to add a courier to the courier list variable
    menu_stars()
    print("What courier would you like to add?")
    menu_stars()
    x = input("Courier: ")
    if x == "0" or x.lower() == "exit":
        print("Exiting to Courier Menu")
        courier_menu()
    else:
        add_courier_input(x)
def change_courier(): # Changes a courier on the list to a new variable specified by user
    global courier_list
    menu_stars()
    print("Courier Names with Numbers")
    menu_stars()
    sort_couriers()
    print_couriers()
    print("Which courier number would you like to change?")
    n = input("Courier name: ")
    if n == "0" or n.lower() == "exit":
        courier_menu()
    elif int(n) - 1 <= len(courier_list):
        print("What would you like to change it to?")
        x = input("New Name: ")
        courier_list[int(n)-1] = x
        change_courier()
    else:
        print("Sorry, I don't recognise that command. Type help to show a list of available commands")
        change_courier()
def delete_courier(): # Prints product list and deletes an item from the list based on index 
    global courier_list
    menu_stars()
    print("Delete a Courier from List")
    menu_stars()
    print_couriers()
    print("Which courier would you like to delete?")
    x = input("Courier Number: ")
    if x == "0" or x == "exit":
        courier_menu()
    elif int(x) - 1 < len(courier_list) and int(x) > 0:
        print("Confirm you wish to delete {}? (Y or N)".format(courier_list[int(x)-1])) #Confirmation to delete otherwise return to top of menu
        n = input("Confirm?: ")
        if n.lower() == "y":
            courier_list.pop(int(x) - 1)
            delete_courier()
        elif n.lower() == "n":
            delete_courier()
        else:
            print("Invalid Entry. Returning to Menu")
            delete_courier()
#endregion
#region Variable_Block
product_list = sorted(data.product_data_load())
courier_list = sorted(data.courier_data_load())
#endregion
try:
    main_menu()
except:
    data.product_data_save(product_list)
    data.courier_data_save(courier_list)
    print("An error has occured. Exiting Program")