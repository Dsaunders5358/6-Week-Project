#region Function Block
def add_new_product():
    name = input("Name: ").title()
    if name == "0" or len(name) <= 0: return "cancel"
    print(f"Please enter price of {name}")
    price = input("Price: £")
    if price == "0" or len(price) <= 0: return "cancel"
    new_product = {"id" : str(len(products_list) + 1), "name" : name, "price" : price}
    products_list.append(new_product)
def delete_product():
    index = input("Index: ")
    try:
        if int(index) - 1 >= 0 and int(index) - 1 < len(products_list):
            products_list.pop(int(index) - 1)
            return "success"
        elif index == "0":
            return "exit"
        else:
            return "none"
    except ValueError:
        return "error"
def update_product(index):
    new_index = check_if_range(index, products_list)
    if new_index == "cancel": return "cancel"
    elif new_index == "error": return "error"
    print("Please input what would you would to change for name and price")
    print("Leave Blank leave field as is or type 0 to cancel and return to menu")
    input_name = input("Change {} to: ".format(products_list[new_index]["name"]))
    if len(input_name) < 0:
        print("No Change")
    elif input_name == "0":
        return "cancel"
    else:
        products_list[int(index) - 1]["name"] = input_name
    input_price = input("Change £{} to: £".format(products_list[int(index) - 1]["price"]))
    if len(input_price) <= 0:
            print("No Change")
    else:
        products_list[int(index) - 1]["price"] = input_price
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
#endregion
#region Variable Block
products_list = []
#endregion