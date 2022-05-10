products_list = [{"name" : "Cheese", "price" : "0.50" }, {"name" : "Pickle", "price" : "1.00" }]
products_list[0] = {"name" : "Bread", "price" : "0.75"}

def test_function():
    return "Cheese", "Bread"
name1, name2 = test_function()
print(name1)
print(name2)