import pymysql
import os
from dotenv import load_dotenv
#region Function Block
def add_new_courier(): # Format courier and add to list
    name = input("Name: ").title()
    if name == "0" or len(name) <= 0: return "cancel"
    print(f"Please enter phone number of {name}")
    num = input("Number: ")
    try:
        int(num)
    except:
        return "error"
    if num == "0" or len(num) <= 0: return "cancel"
    new_courier = {"id" : str(len(couriers_list) + 1),  "name" : name, "number" : num}
    couriers_list.append(new_courier)
def delete_courier(): # Pop courier from list
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
    new_index = check_if_range(index, couriers_list)
    if new_index == "cancel": return "cancel"
    elif new_index == "error": return "error"
    print("Please input to change for name and number")
    print("Leave Blank leave field as is or type 0 to cancel and return to menu")
    input_name = input("Change {} to: ".format(couriers_list[new_index]["name"]))
    if len(input_name) <= 0:
        print("No Change")
    elif input_name == "0":
        return "cancel"
    else:
        couriers_list[new_index]["name"] = input_name
    input_num = input("Change {} to: ".format(couriers_list[new_index]["number"]))
    if len(input_num) <= 0:
            print("No Change")
    else:
        couriers_list[new_index]["number"] = input_num
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
def print_courier_data():
    cursor = connection.cursor()
    cursor.execute('SELECT * from couriers')
    couriers = cursor.fetchall()
    for count, row in enumerate(couriers, 1):
        if count > 9:
            print(f"{count} | {row[1]} | {row[2]}")
        else:
            print(f"{count}  | {row[1]} | {row[2]}")
    cursor.close()
    connection.close()
#endregion
#region Variable Block
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
couriers_list = []
#endregion