couriers_list = [{"name" : "Joe Bloggs", "number" : "0754561023"}, {"name" : "Jane Doe", "number" : "042316578"}]
def add_new_courier():
    name = input("Name: ").title()
    if name == "0" or len(name) <= 0: return "cancel"
    print("Please enter price of {name}")
    price = input("Price: £")
    if price == "0" or len(price) <= 0: return "cancel"
    new_courier = {"name" : name, "price" : price}
    couriers_list.append(new_courier)
def delete_courier():
    index = input("Index: ")
    try:
        if int(index) - 1 >= 0 and int(index) - 1 < len(couriers_list):
            couriers_list.pop(int(index) - 1)
            return "success"
        elif index == "0":
            return "exit"
        else:
            return "none"
    except ValueError:
        return "error"
def update_courier(index):
    print("Please input what would you would to change for name and price")
    print("Leave Blank leave field as is or type 0 to cancel and return to menu")
    input_name = input("Change {} to: ".format(couriers_list[int(index) - 1]["name"]))
    if len(input_name) <= 0:
        print("No Change")
    elif input_name == "0":
        return "cancel"
    else:
        couriers_list[int(index) - 1]["name"] = input_name
    input_price = input("Change {} to: ".format(couriers_list[int(index) - 1]["price"]))
    if len(input_price) <= 0:
            print("No Change")
    else:
        couriers_list[int(index) - 1]["price"] = input_price
    return "success"