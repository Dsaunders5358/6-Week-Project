#region Import Block
import products, couriers
#endregion
#region Function Block
def add_order_input():
    print("Entering details for a new order. Type 0 in any field to cancel and exit to main orders menu")
    name, address, number = get_customer_name()
    if name =="cancel" or address == "cancel" or number == "cancel": return "cancel"
    customer_products = get_order_products()
    courier_name = get_order_couriers()
    order_dict = {
        "customer_name" : name,
        "customer_address" : address,
        "customer_phone" : number,
        "courier" : courier_name,
        "status" : "preparing", 
        "items" : customer_products, 
    }
    orders_list.append(order_dict)
def get_customer_name():
    print("Please enter customers name")
    name = input("Name: ")
    if name =="0":
        return "cancel", "cancel", "cancel"
    print("Please enter customers address")
    address = input("Address: ")
    if address =="0":
        return "cancel", "cancel", "cancel"
    print("Please enter customer's phone number")
    number = input("Number: ")
    if number =="0":
        return "cancel", "cancel", "cancel"
    return name, address, number
def get_order_products():
    repeat = ""
    customer_products = []
    while repeat != "n":
        for counter, item in enumerate(products.products_list, 1): # Prints all product dicts in numbered list with formatting <1st field> | <2nd field> 
            print("{}) ".format(counter) + " | ".join(str(value)for value in item.values()))
        print("Which product index would you like to add to order?")
        input_index = input("Index: ")
        if input_index == "cancel": return "cancel"
        new_index = check_if_range(input_index, products.products_list)
        customer_products.append(products.products_list[new_index]["name"])
        print("Do you want to add another product to order?. Type N to finish adding items")
        repeat = input("Add more products?: ")
    return customer_products
def get_order_couriers():
    for counter, item in enumerate(couriers.couriers_list, 1): # Prints all courier dicts in numbered list with formatting <1st field> | <2nd field> 
        print("{}) ".format(counter) + " | ".join(str(value)for value in item.values()))
    print("Please type number of courier you would like to add")
    input_index = input("Index: ")
    new_index = check_if_range(input_index, couriers.couriers_list)
    return couriers.couriers_list[new_index]["name"] 
def update_order_status():
    print("Type index of order you would to update the status of. Type 0 to exit to orders menu")
    index = input("Order: ")
    new_index = check_if_range(index, orders_list)
    print("What would you like to change status to?")
    new_status = input("Status: ")
    orders_list[new_index]["status"] = new_status
def update_order_details():
    print("Type index of order you would to update the details of. Type 0 to exit to orders menu")
    input_index = input("Order: ")
    new_index = check_if_range(input_index, orders_list)
    headers = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
    for field in headers:
        print(orders_list[new_index][field])
        if field == "items":
            print("Would you like to change the products for order. Y or N")
            confirm = input("Y or N")
            while confirm.lower() != "y" and confirm.lower() != "n":
                print("Invalid response. Please type Y or N")
                confirm = input("Y or N")
            if confirm.lower() == "y":
                new_products = get_order_products()
                orders_list[new_index][field] = new_products
            continue    
        new_field = input(f"Change {field}: ")
        if new_field == "0":
            return "cancel"
        elif len(new_field) > 0:
            orders_list[new_index][field] = new_field.title()
    print(" " + " | ".join(str(value)for value in orders_list[new_index].values()))      
def remove_courier():
    print("Type index of order you would to remove the courier of. Type 0 to exit to orders menu")
    index_input = input("Order: ")
    new_index = check_if_range(index_input, orders_list)
    if new_index == "cancel":
        return "cancel"
    orders_list[new_index]["courier"] = "N/A"
    return "success"
def check_if_range(index, list): # Checks if input is digit, will run untill input is digit
    list_index = -1
    if index == "0":
        return "cancel"
    while index.isdigit() == False or (list_index < 0 and list_index > len(list)):
        print("Im here")
        index = input("Index: ")
        if index.isdigit() == False:
            while index.isdigit() == False:
                index = input("Index: ")
                print("Invalid input. Please input valid number to continue")
        list_index = int(index) - 1
        if list_index < 0 or list_index > len(list):
            print("Index not found. Please input valid number")
            continue
    list_index = int(index) - 1
    return list_index
#endregion
#region Variable Block        
orders_list = []
#endregion