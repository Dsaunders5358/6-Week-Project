#import couriers
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