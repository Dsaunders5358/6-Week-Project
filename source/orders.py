import products, couriers

def add_order_input():
    print("Entering details for a new order. Type 0 in any field to cancel and exit to main orders menu")
    name, address, number = get_customer_name()
    if name =="cancel" or address == "cancel" or number == "cancel":
        return "cancel"
    end_loop = ""
    customer_products = []
    while end_loop.lower() != "n":
        for counter, item in enumerate(products.products_list, 1): # Prints all product dicts in numbered list with formatting <1st field> | <2nd field> 
            print("{}) ".format(counter) + " | ".join(str(value)for value in item.values()))
        print("Which Product index would you like to add to order")
        product = int(input("Index: ")) - 1
        customer_products.append(products.products_list[product]["name"])
        print("Would you like to add another product? (Y or N)")
        end_loop = input("Y or N: ")
        while end_loop.lower() != "y" and end_loop.lower() != "n":
            print("Invalid Command, Please enter N to continue or Y to add new product")
            end_loop = input("Y or N: ")
    for counter, item in enumerate(couriers.couriers_list, 1): # Prints all courier dicts in numbered list with formatting <1st field> | <2nd field> 
        print("{}) ".format(counter) + " | ".join(str(value)for value in item.values()))
    print("Which courier index would you like to assign to this order")
    courier_id = int(input("Index: ")) - 1
    courier_name = couriers.couriers_list[courier_id]["name"]
    order_dict = {
        "customer_name" : name,
        "customer_address" : address,
        "customer phone" : number,
        "courier" : courier_name,
        "status" : "preparing", 
        "items" : customer_products, 
    }
    print(order_dict)
    orders_list.append(order_dict)
    print (orders_list)
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
orders_list = []