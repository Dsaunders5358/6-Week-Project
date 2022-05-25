def test_add_couriers():
    def add_new_courier(name, num): # Format courier and add to list
        if name == "0" or len(name) <= 0: return "cancel"
        new_courier = {"name" : name, "number" : num}
        couriers_list.append(new_courier)
    couriers_list = []
    expected = [{"name" : "charlie", "number" : "0121"}]
    add_new_courier("charlie", "0121")
    actual = couriers_list
    assert actual == expected
def test_add_couriers_blank():
    def add_new_courier(name, num):
        if name == "0" or len(name) <= 0: return "cancel"
        new_courier = {"name" : name, "number" : num}
        couriers_list.append(new_courier)
    couriers_list = []
    expected = []
    add_new_courier("", "0121")
    actual = couriers_list
    assert actual == expected
def test_add_couriers_cancel():
    def add_new_courier(name, num):
        if name == "0" or len(name) <= 0: return "cancel"
        new_courier = {"0" : name, "number" : num}
        couriers_list.append(new_courier)
    couriers_list = []
    expected = "cancel"
    actual = add_new_courier("", "0121")
    assert actual == expected
def test_check_if_range_number():
    index_input = "5"
    data_list = [4, 5, 7, 4, 6, "Cherry"]
    def range_check(index_input, data_list): # Checks if input is digit
        if index_input.isdigit() == True:
            if int(index_input) - 1 < 0 or int(index_input) - 1 > len(data_list):
                return "error"
            elif index_input == "0":
                return "cancel"
            else:
                return int(index_input) - 1
        else:
            return "error"
    actual = range_check(index_input, data_list)
    expected = 4
    assert expected == actual
def test_check_if_range_letter():
    index_input = "not a number"
    data_list = [4, 5, 7, 4, 6, "Cherry"]
    def range_check(index_input, data_list): # Checks if input is digit
        if index_input.isdigit() == True:
            if int(index_input) - 1 < 0 or int(index_input) - 1 > len(data_list):
                return "error"
            elif index_input == "0":
                return "cancel"
            else:
                return int(index_input) - 1
        else:
            return "error"
    actual = range_check(index_input, data_list)
    expected = "error"
    assert expected == actual
def test_check_if_range_oor():
    index_input = "12"
    data_list = [4, 5, 7, 4, 6, "Cherry"]
    def range_check(index_input, data_list): # Checks if input is digit
        if index_input.isdigit() == True:
            if int(index_input) - 1 < 0 or int(index_input) - 1 > len(data_list):
                return "error"
            elif index_input == "0":
                return "cancel"
            else:
                return int(index_input) - 1
        else:
            return "error"
    actual = range_check(index_input, data_list)
    expected = "error"
    assert expected == actual
