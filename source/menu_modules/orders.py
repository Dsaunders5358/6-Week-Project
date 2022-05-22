#region Import Block
import source.menu_modules.products as products
import source.menu_modules.couriers as couriers
#endregion
#region Function Block
def add_order_input():
    print("Entering details for a new order. Type 0 in any field to cancel and exit to main orders menu")
    name, address, number = get_customer_name()
    if name =="cancel" or address == "cancel" or number == "cancel": return "cancel"
    customer_products = get_order_products()
    if customer_products == "error":
        return "error"
    courier_name = get_order_couriers()
    if courier_name == "error":
        return "error"
    order_dict = {
        "id" : str(len(orders_list) + 1), 
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
            print(" | ".join(str(value)for value in item.values()))
        print("Which product index would you like to add to order?")
        input_index = input("Index: ")
        while len(input_index) == 0:
            print("No input, please enter index")
            input_index = input("Index: ")
        new_index = check_if_range(input_index, products.products_list)
        if new_index == "error": return "error"
        elif input_index == "cancel": return "cancel"
        customer_products.append(new_index + 1)
        print("Do you want to add another product to order?. Type N to finish adding items")
        repeat = input("Add more products?: ")
    return customer_products
def get_order_couriers():
    for counter, item in enumerate(couriers.couriers_list, 1): # Prints all courier dicts in numbered list with formatting <1st field> | <2nd field> 
        print("{}) ".format(counter) + " | ".join(str(value)for value in item.values()))
    print("Please type number of courier you would like to add")
    input_index = input("Index: ")
    while len(input_index) == 0:
        print("No input, please enter index")
        input_index = input("Index: ")
    new_index = check_if_range(input_index, couriers.couriers_list)
    if new_index == "error": return "error"
    elif new_index == "cancel": return "cancel"
    return new_index + 1
def update_order_status():
    print("Type index of order you would to update the status of. Type 0 to exit to orders menu")
    index = input("Order: ")
    while len(index) == 0:
        print("No input, please enter index")
        index = input("Index: ")
    new_index = check_if_range(index, orders_list)
    if new_index == "cancel":
        return "cancel"
    new_status = get_new_status()
    if new_status == "cancel":
        return "cancel"
    elif new_status == "error":
        return "error"
    orders_list[new_index]["status"] = new_status
def update_order_details():
    print("Type index of order you would to update the details of. Type 0 to exit to orders menu")
    input_index = input("Order: ")
    while len(input_index) == 0:
        print("No input, please enter index")
        input_index = input("Index: ")
    new_index = check_if_range(input_index, orders_list)
    if new_index == "cancel": return "cancel"
    elif new_index == "error": return "error"
    headers = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
    for field in headers:
        print(orders_list[new_index][field])
        if field == "items":
            print("Type Y to show products list to add products. Anything else will skip")
            confirm = input("Products?: ")
            if confirm.lower() != "y":
                continue
            else:
                new_products = get_order_products()
                if new_products == "error": return "error"
                elif new_products == "cancel": return "cancel"
                orders_list[new_index][field] = new_products
                continue
        elif field == "status":
            print("Type Y to show status list to change status. Anything else will skip")
            confirm = input("Status?: ")
            if confirm.lower() != "y":
                continue
            else:
                new_status = get_new_status()
                if new_status == "error": return "error"
                elif new_status == "cancel": return "cancel"
                orders_list[new_index][field] = status_list[new_status]
                continue
        elif field == "courier":
            print("Type Y to show courier list to add courier. Anything else will skip")
            confirm = input("Couriers?: ")
            if confirm.lower() != "y":
                continue
            else:
                new_courier = get_order_couriers()
                if new_courier == "error": return "error"
                elif new_courier == "cancel": return "cancel"
                orders_list[new_index][field] = new_courier
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
    elif new_index == "error":
        return "error"
    orders_list[new_index]["courier"] = "N/A"
    return "success"
def check_if_range(index, list): # Checks if input is digit
    if index.isdigit() == True:
        if int(index) - 1 < 0 or int(index) - 1 > len(list):
            return "error"
        elif index == "0":
            return "cancel"
        else:
            return int(index) - 1
    else:
        return "error"
def get_new_status():
    for count, status in enumerate(status_list, 1):
        print(f"{count} | {status}")
    print("What index would you like to change status to? Type 0 to cancel")
    index = input("Status: ")
    while len(index) == 0:
            print("No input, please enter index")
            index = input("Index: ")
    new_status = check_if_range(index, status_list)
    if new_status == "cancel":
        return "cancel"
    elif new_status == "error":
        return "error"
    return status_list[new_status]
def delete_order():
    print("Type index of order you wish to remove. Type 0 to cancel")
    index = input("Order: ")
    while len(index) == 0:
        print("No input, please enter index")
        index = input("Index: ")
    order_remove = check_if_range(index, orders_list)
    if order_remove == "cancel":
        return "cancel"
    elif order_remove == "error":
        return "error"
    orders_list.pop(order_remove)
#endregion
#region Variable Block        
orders_list = []
status_list = ["Preparing", "Out for delivery", "Delivered", "Cancelled"]
test_list = [{"status" : "Preparing"}, {"status" : "Out for delivery"}, {"status" : "Delivered"}, {"status" : "Cancelled"}]
#endregion