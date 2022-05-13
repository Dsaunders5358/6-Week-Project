import products, couriers
def add_order_input():
    print("Entering details for a new order. Type 0 in any field to cancel and exit to main orders menu")
    name, address, number = get_customer_name()
    if name =="cancel" or address == "cancel" or number == "cancel":
        return "cancel"
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
        product = input("Index: ")
        if product.isdigit() == False:
            while product.isdigit() == False:
                product = input("Index: ")
                print("Invalid input. Please input valid number to continue")
        list_index = int(product) - 1
        if list_index < 0 and list_index > len(products.products_list):
            print("Index not found. Rerunning products list.")
            continue
        else:
            customer_products.append(products.products_list[list_index]["name"])
        print("Do you want to add another product to order?. Type N to finish adding items")
        repeat = input("Add more products?: ")
    return customer_products
def get_order_couriers():
    for counter, item in enumerate(couriers.couriers_list, 1): # Prints all courier dicts in numbered list with formatting <1st field> | <2nd field> 
        print("{}) ".format(counter) + " | ".join(str(value)for value in item.values()))
    print("Please type number of courier you would like to add")
    courier = ""
    list_index = ""
    while courier.isdigit() == False or list_index < 0 or list_index > len(couriers.couriers_list):
        courier = input("Index: ")
        if courier.isdigit() == False:
            while courier.isdigit() == False:
                courier = input("Index: ")
                print("Invalid input. Please input valid number to continue")
        list_index = int(courier) - 1
        if list_index < 0 or list_index > len(couriers.couriers_list):
            print("Index not found. Please input valid number")
            continue
    return couriers.couriers_list[list_index]["name"] 
def update_order_status():
    print("Type index of order you would to update the status of. Type 0 to exit to orders menu")
    index = input("Order: ")
    list_index = -1
    if index == "0":
        return "cancel"
    while index.isdigit() == False or (list_index < 0 and list_index > len(orders_list)):
        index = input("Index: ")
        if index.isdigit() == False:
            while index.isdigit() == False:
                index = input("Index: ")
                print("Invalid input. Please input valid number to continue")
        list_index = int(index) - 1
        if list_index < 0 or list_index > len(orders_list):
            print("Index not found. Please input valid number")
            continue
    print("What would you like to change status to?")
    new_status = input("Status: ")
    orders_list[list_index]["status"] = new_status
def update_order_details():
    print("Type index of order you would to update the details of. Type 0 to exit to orders menu")
    index = input("Order: ")
    list_index = -1
    if index == "0":
        return "cancel"
    while index.isdigit() == False or (list_index < 0 and list_index > len(orders_list)):
        index = input("Index: ")
        if index.isdigit() == False:
            while index.isdigit() == False:
                index = input("Index: ")
                print("Invalid input. Please input valid number to continue")
        list_index = int(index) - 1
        if list_index < 0 or list_index > len(orders_list):
            print("Index not found. Please input valid number")
            continue
    print("Running through each field individually. Leave blank to make no changes to that field")
    print(orders_list[list_index]["customer_name"])
    new_name = input("Change name: ")
    if len(new_name) > 0:
        orders_list[list_index]["customer_name"] = new_name
    print(orders_list[list_index]["customer_address"])
    new_address = input("Change address: ")
    if len(new_address) > 0:
        orders_list[list_index]["customer_address"] = new_address
    print(orders_list[list_index]["customer_phone"])
    new_phone = input("Change number: ")
    if len(new_phone) > 0:
        orders_list[list_index]["customer_phone"] = new_phone
    print(orders_list[list_index]["courier"])
    new_courier = input("Change courier: ")
    if len(new_courier) > 0:
        orders_list[list_index]["courier"] = new_courier
    print(orders_list[list_index]["status"])
    new_status = input("Change status: ")
    if len(new_status) > 0:
        orders_list[list_index]["status"] = new_status
    print("Would you like to change the products for order. Y or N")
    confirm = input("Y or N")
    while confirm.lower() != "y" and confirm.lower() != "n":
        print("Invalid response. Please type Y or N")
        confirm = input("Y or N")
    if confirm.lower() == "y":
        new_products = get_order_products()
        orders_list[list_index]["items"] = new_products
    print(" " + " | ".join(str(value)for value in orders_list[list_index].values()))
def remove_courier():
    print("Type index of order you would to remove the courier of. Type 0 to exit to orders menu")
    index = input("Order: ")
    list_index = -1
    if index == "0":
        return "cancel"
    while index.isdigit() == False or (list_index < 0 and list_index > len(orders_list)):
        print("Invalid input. Please input valid number to continue")
        index = input("Index: ")
        if index == "0":
            return "cancel"
        if index.isdigit() == False:
            while index.isdigit() == False:
                index = input("Index: ")
        list_index = int(index) - 1
        if list_index < 0 or list_index > len(orders_list):
            print("Index not found. Please input valid number")
            continue
    orders_list[list_index]["courier"] = "N/A"
    return "success"
orders_list = []