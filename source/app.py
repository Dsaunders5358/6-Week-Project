#region Import Blocks
import logging
import source.menu_modules.products as products
import source.menu_modules.couriers as couriers
import source.menu_modules.orders as orders
import source.data_handlers.csv_data as data
import source.data_handlers.sql_data as sql_data
#endregion
#region Function Blocks
def program_start(): #Program run loop. Saves data to CSV when done
    menu = show_main_menu()
    while menu != "exit":
        menu = move_to_menu(menu)
    print("Exiting App\nGoodbye")
    sql_data.save_to_csv("products_list.csv")
    sql_data.save_to_csv("couriers_list.csv")
    sql_data.save_to_csv("orders_list.csv")
def generate_menu_options(*options):
    index = 1
    for option in options:
        print(f"{index} | {option}")
        index += 1
    print("0 | Exit")
def print_title_stars(title):  #Formatting stars via title
    stars = ""
    for char in range(0, len(title)):
        stars += "*"
    print(stars)
    print(title)
    print(stars)
def show_main_menu():  # First menu user will see
    print_title_stars("Main Menu")
    print("Please Choose a Menu Option.\n1 | Products\n2 | Couriers\n3 | Orders\n0 | Exit Program")
    nav = input("Option: ")
    if nav == "1":
        return "products main"
    elif nav == "2":
        return "couriers main"
    elif nav == "3":
        return "orders main"
    elif nav == "0":
        return "exit"
    else:
        print("Command not recognised. Returning to menu")
        return "main menu"
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
    elif menu == "orders delete":
        return show_orders_del_order_menu()
def show_type_main_menu(type):
    print_title_stars("{} menu".format(type.title())) 
    generate_menu_options(f"Show current {type}s",f"Add new {type}" , f"Update Existing {type}s", f"Delete a {type}")
    print("Please choose an option")
    nav = input("Option: ")
    if nav == "1":
        if type == "product":
            sql_data.get_products_data()
        elif type == "courier":
            sql_data.get_couriers_data()
        input("Press Enter to Continue")
        return f"{type}s main"
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
    print("Leave field blank or type 0 to exit")
    print("Please enter name of new product to add")
    cancel = products.add_new_product()
    if cancel == "cancel":
        print("Cancelling input. Returning to products menu")
    elif cancel == "error":
        print("Invalid Input. Returning to products menu")    
    else:
        print("Product successfully added. Returning to products Menu")
    return "products main"
def show_product_del_menu():
    print_title_stars("Delete a Product")
    data_list = sql_data.get_products_data()
    print("Type index of product you wish to delete. 0 will exit")
    delete = products.delete_product(data_list)
    if delete == "exit":
        print("Cancelling delete. Returning to products menu")
    elif delete == "error":
        print("Invalid Command. Returning to Products Menu")
    elif delete == "success":
        print("Product removed successfully. Returning to products menu")
    elif delete == "none":
        print("Index not found. Returning to products menu")
    return "products main"
def show_product_update_menu():
    print_title_stars("Update a product")
    get_list = sql_data.get_products_data()
    print("Type index of product you wish to change. 0 will exit")
    update = input("Option: ")
    confirm = products.update_product(update, get_list)
    if confirm == "cancel":
        print("Cancelling Changes. Returning to products menu")
    elif confirm == "success":
        print("Change Successful. Returning to products menu")
    elif confirm == "error":
        print("Invalid index input. Returning to products menu")
    return "products main"
def show_courier_add_menu():
    print_title_stars("Add New Courier Menu")
    print("Leave field blank or type 0 to exit")
    print("Please enter name of new product to add")
    cancel = couriers.add_new_courier()
    if cancel == "cancel":
        print("Cancelling input. Returning to courier menu")
    elif cancel == "error":
        print("Invalid input, Returning to couriers menu")
    else:
        print("Courier successfully added. Returning to couriers Menu")
    return "couriers main"
def show_courier_del_menu():
    print_title_stars("Delete a Courier")
    data_list = sql_data.get_couriers_data()
    print("Type index of courier you wish to delete. 0 will exit")
    delete = couriers.delete_courier(data_list)
    if delete == "exit":
        print("Cancelling delete. Returning to couriers menu")
    elif delete == "error":
        print("Invalid Command. Returning to couriers Menu")
    elif delete == "success":
        print("Courier removed successfully. Returning to couriers menu")
    elif delete == "none":
        print("Index not found. Returning to couriers menu")
    return "couriers main"
def show_courier_update_menu():
    print_title_stars("Update a courier")
    get_list = sql_data.get_couriers_data()
    print("Type index of courier you wish to change. 0 will exit")
    update = input("Option: ")
    confirm = couriers.update_courier(update, get_list)
    if confirm == "cancel":
        print("Cancelling Changes. Returning to couriers menu")
    elif confirm == "success":
        print("Change Successful. Returning to couriers menu")
    elif confirm == "error":
        print("Invalid index entered. Returning to couriers menu")
    return "couriers main"
def show_orders_main_menu():
    print_title_stars("Orders Main Menu")
    generate_menu_options("Show Existing Orders", "Add new order", "Update order status", "Update order details", "Delete Courier from Order", "Delete Whole Order")
    print("Please choose an option")
    nav = input("Option: ")
    if nav == "1":
        sql_data.get_orders_data()
        input("Press enter to continue")
        return "orders main"
    elif nav == "2":
        return "orders add"
    elif nav == "3":
        return "orders status"
    elif nav == "4":
        return "orders update"
    elif nav == "5":
        return "orders del courier"
    elif nav == "6":
        return "orders delete"
    elif nav == "0":
        return "main menu"
    else:
        print("Invalid option. Please enter a valid number.")
        return "orders main"
def show_orders_add_menu():
    print_title_stars("Add New Order Menu")
    status = orders.add_order_input()
    if status == "cancel":
        print("Order Cancelled. Returning to orders menu")
        return "orders main"
    elif status == "error":
        print("Invalid Command Entry or blank field. Returning to orders menu")
        return "orders main"
    print (f"Order has been added. Returning to orders menu")
    return "orders main"
def show_orders_status_menu():
    print_title_stars("Update Order Status")
    status = orders.update_order_status()
    if status == "cancel":
        print("Cancelling change, returning to orders menu")
        return "orders main"
    elif status == "error":
        print("Index Error, Returning to orders menu")
        return "orders main"
    print("order status changed successfully. Returning to orders menu")
    return "orders main" 
def show_orders_update_menu():
    print_title_stars("Updating Order Details")
    changed = orders.update_order_details()
    if changed == "cancel":
        print("Cancelling change. Returning to orders menu")
        return "orders main"
    elif changed == "error":
        print("Invalid command entry. Returning to orders menu")
        return "orders main"
    print("Order details changed successfully")
    return "orders main"
def show_orders_del_courier_menu():
    print_title_stars("Delete Courier from Order")
    data.print_data_list(orders.orders_list)
    removed = orders.remove_courier()
    if removed == "cancel":
        print("Removal Cancelled. Returning to orders menu")
        return "orders main"
    elif removed == "error":
        print("Invalid command entry. Returning to orders menu")
        return "orders main"
    print("Courier successfully removed from order")
    return "orders main"
def show_orders_del_order_menu():
    print_title_stars("Delete Entire Order")
    data.print_data_list(orders.orders_list)
    removed = orders.delete_order()
    if removed == "cancel":
        print("Removal Cancelled. Returning to orders menu")
        return "orders main"
    elif removed == "error":
        print("Invalid command entry. Returning to orders menu")
        return "orders main"
    print("Order Successfully deleted. Returning to orders menu")
    return "orders main"
#endregion
#region Variable Block
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
#endregion
try:
    program_start()
except KeyboardInterrupt:
    print("Debug Finished. Exiting") 
except Exception as log:
    logger.exception(log)
    sql_data.save_to_csv("products_list.csv")
    sql_data.save_to_csv("couriers_list.csv")
    #data.save_csv_data(orders.orders_list, "orders.csv")
    print("Unkown Error has Occured. Saving data and exiting application")