#import couriers
def test_add_couriers(name, num):
    couriers_list = []
    expected = [{"name" : name, "number" : num}]
    
    def add_new_courier(name, num): # Format courier and add to list
        if name == "0" or len(name) <= 0: return "cancel"
        new_courier = {"name" : name, "number" : num}
        couriers_list.append(new_courier)
    add_new_courier(name, num)
    actual = couriers_list
    assert actual == expected
    print("Success")