products_list = [{"name" : "Cheese", "price" : "0.50" }, {"name" : "Pickle", "price" : "1.00" }]
products_list[0] = {"name" : "Bread", "price" : "0.75"}
key_list = []
input_test = "5.64"
while type(input_test) == type("string"):
    try:
        input_test > 0
    except:
        input_test = float(input_test)
print("This is now not a string")