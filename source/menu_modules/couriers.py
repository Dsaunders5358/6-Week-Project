import source.data_handlers.sql_data as sql_data
#region Function Block
def add_new_courier():
    name = input("Name: ").title()
    if name == "0" or len(name) <= 0: return "cancel"
    print(f"Please enter number of {name}")
    num = input("number: ")
    if num == "0" or len(num) <= 0: return "cancel"
    sql_data.add_courier_data(name, num)
def delete_courier(data_list): # Pop courier from list
    index = input("Index: ")
    new_index = check_if_range(index, data_list)
    if new_index >= 0 and new_index < len(data_list):
        sql_data.remove_courier_data(new_index)
        return "success"
    elif index == "0":
        return "exit"
    else:
        return "none"
def update_courier(index, data_list):
    new_index = check_if_range(index, data_list)
    if new_index == "cancel": return "cancel"
    elif new_index == "error": return "error"
    print("Please input the change for name and number")
    print("Leave Blank to leave each option as it is or type 0 to cancel and return to menu")
    input_name = input("Change name to: ")
    if len(input_name) < 0:
        print("No Change")
    elif input_name == "0":
        return "cancel"
    input_num = input("Change number to: ")
    if len(input_num) <= 0:
            print("No Change")
    sql_data.update_courier_data(new_index, input_name, input_num)
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
#endregion