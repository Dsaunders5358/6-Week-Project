products_list = [{"name" : "Cheese", "price" : "0.50" }, {"name" : "Pickle", "price" : "1.00" }]
products_list[0] = {"name" : "Bread", "price" : "0.75"}
key_list = []

for key in products_list[0].keys():
    key_list.append(key)
print(key_list)