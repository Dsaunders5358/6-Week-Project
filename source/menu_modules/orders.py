#region Import Block
import source.menu_modules.products as products
import source.menu_modules.couriers as couriers
import source.data_handlers.sql_data as sql_data
#endregion
#region Function Block
def add_order_input():
    print("Entering details for a new order. Type 0 in any field to cancel and exit to main orders menu")
    name, address, number = get_customer_name()
    if name =="cancel" or address == "cancel" or number == "cancel": return "cancel"
    elif name =="error" or address == "error" or number == "error": return "error"
    product_id = get_order_products()
    if product_id == "error":
        return "error"
    courier_id = get_order_couriers()
    if courier_id == "error":
        return "error"
    sql_data.add_order_data(name, address, number, courier_id, product_id)
def get_customer_name():
    print("Please enter customers name")
    name = input("Name: ")
    if name =="0":
        return "cancel", "cancel", "cancel"
    elif len(name) <= 0:
        return "error", "error", "error"
    print("Please enter customers address")
    address = input("Address: ")
    if address =="0":
        return "cancel", "cancel", "cancel"
    elif len(address) <= 0:
        return "error", "error", "error"
    print("Please enter customer's phone number")
    number = input("Number: ")
    if number =="0":
        return "cancel", "cancel", "cancel"
    elif len(number) <= 0:
        return "error", "error", "error"
    return name, address, number
def get_order_products():
    #repeat = ""
    #customer_products = []
    #while repeat != "n":
    data_list = sql_data.get_products_data()
    print("Which product index would you like to add to order?")
    input_index = input("Index: ")
    while len(input_index) == 0:
        print("No input, please enter index")
        input_index = input("Index: ")
    new_index = check_if_range(input_index, data_list)
    if new_index == "error": return "error"
    elif input_index == "cancel": return "cancel"
    customer_products = new_index + 1
    #print("Do you want to add another product to order?. Type N to finish adding items")
    #repeat = input("Add more products?: ")
    return customer_products
def get_order_couriers():
    data_list = sql_data.get_couriers_data()
    print("Please type number of courier you would like to add")
    input_index = input("Index: ")
    while len(input_index) == 0:
        print("No input, please enter index")
        input_index = input("Index: ")
    new_index = check_if_range(input_index, data_list)
    if new_index == "error": return "error"
    elif new_index == "cancel": return "cancel"
    return new_index + 1
def update_order_status():
    data_list = sql_data.get_orders_data()
    print("Type index of order you would to update the status of. Type 0 to exit to orders menu")
    index = input("Order: ")
    while len(index) == 0:
        print("No input, please enter index")
        index = input("Index: ")
    new_index = check_if_range(index, data_list)
    if new_index == "cancel":
        return "cancel"
    new_status = get_new_status()
    if new_status == "cancel":
        return "cancel"
    elif new_status == "error":
        return "error"
    sql_data.update_order_status(data_list[new_index]["order_id"], new_status)
def update_order_details():
    data_list = sql_data.get_orders_data()
    print("Type index of order you would to update the details of. Type 0 to exit to orders menu")
    input_index = input("Order: ")
    while len(input_index) == 0:
        print("No input, please enter index")
        input_index = input("Index: ")
    new_index = check_if_range(input_index, data_list)
    if new_index == "cancel": return "cancel"
    elif new_index == "error": return "error"
    headers = ["customer_name", "customer_address", "customer_phone", "courier_id", "items"]
    for field in headers:
        if field == "customer_name":
            print(field + " | " + data_list[new_index][field])
            print("Type name to change to. Leave blank to not change. 0 to exit and cancel all changes")
            name_input = input("New Name: ")
            if name_input == "0":
                return "cancel"
            else:
                name = name_input
        elif field == "customer_address":
            print(field + " | " + data_list[new_index][field])
            print("Type name to change to. Leave blank to not change. 0 to exit and cancel all changes")
            address_input = input("New Address: ")
            if address_input == "0":
                return "cancel"
            else:
                address = address_input
        elif field == "customer_phone":
            print(field + " | " + data_list[new_index][field])
            print("Type name to change to. Leave blank to not change. 0 to exit and cancel all changes")
            number_input = input("New Number: ")
            if number_input == "0":
                return "cancel"
            else:
                number = number_input
        elif field == "items":
            products_data = sql_data.store_products_data()
            sql_data.get_products_data()
            print(("Choose New Product. Leave blank to not change. 0 to exit and cancel all changes"))
            prod_index = input("New product: ")
            if len(prod_index) <= 0:
                continue
            prod_index = check_if_range(prod_index, products_data)
            if prod_index == "error": return "error"
            elif prod_index == "cancel": return "cancel"
        elif field == "courier_id":
            couriers_data = sql_data.store_couriers_data()
            sql_data.get_couriers_data()
            print(("Choose New Courier. Leave blank to not change. 0 to exit and cancel all changes"))
            courier_index = input("New Courier: ")
            if len(courier_index) <= 0:
                continue
            courier_index = check_if_range(courier_index, couriers_data)
            if courier_index == "error": return "error"
            elif courier_index == "cancel": return "cancel"
    sql_data.update_order_data(
        data_list[new_index]["order_id"],
        name_input,
        address_input,
        number_input,
        prod_index + 1,
        courier_index + 1
        ) 
def remove_courier():
    data_list = sql_data.get_orders_data()
    print("Type index of order you would to remove the courier of. Type 0 to exit to orders menu")
    index_input = input("Order: ")
    new_index = check_if_range(index_input, data_list)
    if new_index == "cancel":
        return "cancel"
    elif new_index == "error":
        return "error"
    sql_data.remove_courier_from_order(data_list[new_index]["order_id"])
    return "success"
def check_if_range(index, data_list): # Checks if input is digit
    if index.isdigit() == True:
        if int(index) - 1 < 0 or int(index) - 1 > len(data_list):
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
    data_list = sql_data.get_orders_data()
    print("Type index of order you wish to remove. Type 0 to cancel")
    index = input("Order: ")
    while len(index) == 0:
        print("No input, please enter index")
        index = input("Index: ")
    order_remove = check_if_range(index, data_list)
    if order_remove == "cancel":
        return "cancel"
    elif order_remove == "error":
        return "error"
    sql_data.remove_order(data_list[order_remove]["order_id"])
#endregion
#region Variable Block        
status_list = ["Preparing", "Out for delivery", "Delivered", "Cancelled"]
#endregion