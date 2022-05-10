products_list = [{"name" : "Cheese", "price" : "0.50" }, {"name" : "Pickle", "price" : "1.00" }]
def add_new_product():
    name = input("Name: ").title()
    if name == "0" or len(name) <= 0: return "cancel"
    print("Please enter price of {name}")
    price = input("Price: £")
    if price == "0" or len(price) <= 0: return "cancel"
    new_product = {"name" : name, "price" : price}
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
