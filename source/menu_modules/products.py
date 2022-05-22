import source.data_handlers.sql_data as sql_data
import pymysql
import os
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
def delete_product(list):
    index = input("Index: ")
    new_index = check_if_range(index, list)
    if new_index >= 0 and new_index < len(list):
        sql_data.remove_product_data(new_index)
        return "success"
    elif index == "0":
        return "exit"
    else:
        return "none"
def update_product(index, list):
    new_index = check_if_range(index, list)
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
    if len(input_price) <= 0:
            print("No Change")
    sql_data.update_product_data(new_index, input_name, input_price)
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
def isfloat(num):
    try:
        float(num)
        return num
    except ValueError:
        return "error"
def print_product_data():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * from products')
    products = cursor.fetchall()
    for count, row in enumerate(products, 1):
        if count > 9:
            print(f"{count} | {row[1]} | £{row[2]}")
        else:
            print(f"{count}  | {row[1]} | £{row[2]}")
    cursor.close()
    connection.close()
#endregion
#region Variable Block
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
def connect_to_database():
    return pymysql.connect(
        host,
        user,
        password,
        database
    )
products_list = []
#endregion