products_list = [{"name" : "Cheese", "price" : 0.50 }, {"name" : "Pickle", "price" : 1.00 , "Third" : "test"}]
first = products_list[0].values()
second = list(products_list[1].values())

print(" | ".join(str(e) for e in second))