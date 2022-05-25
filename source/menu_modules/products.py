import source.data_handlers.sql_data as sql_data
from dotenv import load_dotenv
#region Function Block
def add_new_product():
    name = input("Name: ").title()
    if name == "0" or len(name) <= 0: return "cancel"
    print(f"Please enter price of {name}")
    price = input("Price: £")
    try:
        float(price)
    except ValueError:
        return "error"
    if price == "0" or len(price) <= 0: return "cancel"
    sql_data.add_product_data(name, price)
def delete_product(data_list):
    index = input("Index: ")
    if len(index) <= 0:
        return "error"
    new_index = check_if_range(index, data_list)
    if new_index == "error": return "error"
    elif new_index =="cancel" : return "cancel"
    if new_index >= 0 and new_index < len(data_list):
        sql_data.remove_product_data(new_index)
        return "success"
    elif index == "0":
        return "exit"
    else:
        return "none"
def update_product(index, data_list):
    new_index = check_if_range(index, data_list)
    if new_index == "cancel": return "cancel"
    elif new_index == "error": return "error"
    print("Please input the change for name and price")
    print("Leave Blank to leave each option as it is or type 0 to cancel and return to menu")
    input_name = input("Change name to: ")
    if len(input_name) < 0:
        print("No Change")
    elif input_name == "0":
        return "cancel"
    input_price = input("Change price to: £")
    try:
        float(input_price)
    except ValueError:
        return "error"
    if len(input_price) <= 0:
            print("No Change")
    sql_data.update_product_data(new_index, input_name, input_price)
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
def isfloat(num):
    try:
        float(num)
        return num
    except ValueError:
        return "error"
#endregion