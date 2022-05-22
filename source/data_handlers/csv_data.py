import source.menu_modules.products as products
import source.menu_modules.couriers as couriers
import source.menu_modules.orders as orders
from csv import DictReader, DictWriter
from dotenv import load_dotenv
def save_csv_data(list, file_name):
    dict_data = f"data/{file_name}"
    with open(dict_data, mode = "w") as data:
        if file_name == "couriers_list.csv":
            key_headers = ["courier_id", "courier_name", "number"]
        elif file_name == "products_list.csv":
            key_headers = ["product_id", "product_name", "price"]
        elif file_name == "orders_list.csv":
            key_headers = ["order_id","customer_name", "customer_address", "customer_phone", "courier_id", "status", "product_id"]
        writer = DictWriter(data, fieldnames = key_headers)
        writer.writeheader()
        for num in range(len(list)):
            writer.writerow(list[num])
def load_csv_data(file_name):
    data_path = f"data/{file_name}"
    with open(data_path, "r") as data:
        list = DictReader(data)
        if file_name == "products.csv":
            for row in list:
                products.products_list.append(row)
        elif file_name == "couriers.csv":
            for row in list:
                couriers.couriers_list.append(row)
        elif file_name == "orders.csv":
            for row in list:
                orders.orders_list.append(row)
def print_data_list(list):
    for count, item in enumerate(list):
        if int(item["id"]) < 10:
            print("  | ".join(str(value)for value in item.values()))
        else:
            print(" | ".join(str(value)for value in item.values()))