import products, couriers

def add_order_input():
    print("Entering details for a new order. Type 0 in any field to cancel and exit to main orders menu")
    print("Please enter customers name")
    name = input("Name: ")
    if name =="0":
        return "cancel"
    print("Please enter customers address")
    address = input("Address: ")
    if address =="0":
        return "cancel"
    print("Please enter customer's phone number")
    number = input("Number: ")
    if number =="0":
        return "cancel"
    for counter, item in enumerate(products.products_list, 1):
        print("{}) ".format(counter) + " | ".join(str(value)for value in item.values()))