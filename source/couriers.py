#region Function Block
def add_new_courier(): # Format courier and add to list
    name = input("Name: ").title()
    if name == "0" or len(name) <= 0: return "cancel"
    print(f"Please enter phone number of {name}")
    num = input("Number: ")
    if num == "0" or len(num) <= 0: return "cancel"
    new_courier = {"name" : name, "number" : num}
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
    print("Please input what would you would to change for name and number")
    print("Leave Blank leave field as is or type 0 to cancel and return to menu")
    input_name = input("Change {} to: ".format(couriers_list[int(index) - 1]["name"]))
    if len(input_name) <= 0:
        print("No Change")
    elif input_name == "0":
        return "cancel"
    else:
        couriers_list[int(index) - 1]["name"] = input_name
    input_num = input("Change {} to: ".format(couriers_list[int(index) - 1]["number"]))
    if len(input_num) <= 0:
            print("No Change")
    else:
        couriers_list[int(index) - 1]["number"] = input_num
    return "success"
#endregion
#region Variable Block
couriers_list = []
#endregion