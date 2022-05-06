def save_data(list, file_name):
    with open(file_name, "w") as data:
        for items in list:
            data.write(items + '\n')
def load_data(list):
    type = list + "_list.txt"
    with open(type, "r") as data:
        load_list = []
        data = data.read()
        data = data.splitlines()
        for items in data:
            load_list.append(items)
    return load_list