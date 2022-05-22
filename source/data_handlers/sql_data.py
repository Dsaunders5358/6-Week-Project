import pymysql, os
import source.data_handlers.csv_data as csv_data
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
def connect_to_database():
    return pymysql.connect(
        host,
        user,
        password,
        database
    )
def add_product_data(name, price):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO products(product_name, price) VALUES ('{name}', {price});")
    connection.commit()
    cursor.close()
    connection.close()
def get_products_data():
    list = []
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * from products')
    products = cursor.fetchall()
    for count, row in enumerate(products, 1):
        if count > 9:
            print(f"{count} | {row[1]} | £{row[2]}")
            for_dict = {"product_id" : row[0], "product_name" : row[1], "price" : row[2]}
            list.append(for_dict)
        else:
            print(f"{count}  | {row[1]} | £{row[2]}")
            for_dict = {"product_id" : row[0], "product_name" : row[1], "price" : row[2]}
            list.append(for_dict)
    cursor.close()
    connection.close()
    return list
def get_products_list():
    list = []
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * from products')
    products = cursor.fetchall()
    for count, row in enumerate(products, 1):
        if count > 9:
            for_dict = {"product_id" : row[0], "product_name" : row[1], "price" : row[2]}
            list.append(for_dict)
        else:
            for_dict = {"product_id" : row[0], "product_name" : row[1], "price" : row[2]}
            list.append(for_dict)
    cursor.close()
    connection.close()
    return list
def update_product_data(index, new_name, new_price):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * from products")
    products = cursor.fetchall()
    old_name, old_price = products[index][1], products[index][2]
    if len(new_name) <= 0: new_name = old_name
    if len(new_price) <= 0: new_price = old_price
    cursor.execute(f"UPDATE products set product_name = '{new_name}', price = {new_price} WHERE product_name = '{old_name}' and price = {old_price}")
    connection.commit()
    cursor.close()
    connection.close()
def remove_product_data(index):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * from products")
    products = cursor.fetchall()
    del_name, del_price = products[index][1], products[index][2]
    cursor.execute(f"DELETE FROM products WHERE product_name = '{del_name}' and price = '{del_price}'")
    connection.commit()
    cursor.close()
    connection.close()
def save_to_csv(file_name):
    if file_name == "products_list.csv":
            csv_data.save_csv_data(get_products_list(), file_name)
def get_couriers_data():
    list = []
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * from couriers')
    couriers = cursor.fetchall()
    for count, row in enumerate(couriers, 1):
        if count > 9:
            print(f"{count} | {row[1]} | {row[2]}")
            for_dict = {"courier_id" : row[0], "courier_name" : row[1], "number" : row[2]}
            list.append(for_dict)
        else:
            print(f"{count}  | {row[1]} | £{row[2]}")
            for_dict = {"courier_id" : row[0], "courier_name" : row[1], "number" : row[2]}
            list.append(for_dict)
    cursor.close()
    connection.close()
    return list