import pymysql, os
import source.data_handlers.csv_data as csv_data
from dotenv import load_dotenv
def connect_to_database():
    return pymysql.connect(
        host,
        user,
        password,
        database
    )
def save_to_csv(file_name):
    if file_name == "products_list.csv":
        csv_data.save_csv_data(store_products_data(), file_name)
    elif file_name == "couriers_list.csv":
        csv_data.save_csv_data(store_couriers_data(), file_name)
    elif file_name == "orders_list.csv":
        csv_data.save_csv_data(store_orders_data(), file_name)
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
def store_products_data():
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
            print(f"{count}  | {row[1]} | {row[2]}")
            for_dict = {"courier_id" : row[0], "courier_name" : row[1], "number" : row[2]}
            list.append(for_dict)
    cursor.close()
    connection.close()
    return list
def store_couriers_data():
    data_list = []
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * from couriers')
    couriers = cursor.fetchall()
    for count, row in enumerate(couriers, 1):
        if count > 9:
            for_dict = {"courier_id" : row[0], "courier_name" : row[1], "number" : row[2]}
            data_list.append(for_dict)
        else:
            for_dict = {"courier_id" : row[0], "courier_name" : row[1], "number" : row[2]}
            data_list.append(for_dict)
    cursor.close()
    connection.close()
    return data_list
def update_courier_data(index, new_name, new_num):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * from couriers")
    couriers = cursor.fetchall()
    old_name, old_num = couriers[index][1], couriers[index][2]
    if len(new_name) <= 0: new_name = old_name
    if len(new_num) <= 0: new_num = old_num
    cursor.execute(f"UPDATE couriers set courier_name= '{new_name}', number = '{new_num}' WHERE courier_name = '{old_name}' and number = '{old_num}'")
    connection.commit()
    cursor.close()
    connection.close()
def remove_courier_data(index):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * from couriers")
    couriers = cursor.fetchall()
    del_name, del_num = couriers[index][1], couriers[index][2]
    cursor.execute(f"DELETE FROM couriers WHERE courier_name = '{del_name}' and number = '{del_num}'")
    connection.commit()
    cursor.close()
    connection.close()
def add_courier_data(name, num):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO couriers(courier_name, number) VALUES ('{name}', '{num}');")
    connection.commit()
    cursor.close()
    connection.close()
def get_orders_data():
    data_list = []
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * from orders')
    orders = cursor.fetchall()
    for count, row in enumerate(orders, 1):
        if count > 9:
            print(f"{count} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
            for_dict = {
                "order_id" : row[0],
                "customer_name" : row[1],
                "customer_address" : row[2],
                "customer_phone" : row[3],
                "courier_id" : row[4],
                "status" : row[5],
                "product_id" : row[6]
                }
            data_list.append(for_dict)
        else:
            print(f"{count} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
            for_dict = {
                "order_id" : row[0],
                "customer_name" : row[1],
                "customer_address" : row[2],
                "customer_phone" : row[3],
                "courier_id" : row[4],
                "status" : row[5],
                "product_id" : row[6]
                }
            data_list.append(for_dict)
    cursor.close()
    connection.close()
    return data_list
def store_orders_data():
    data_list = []
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * from orders')
    orders = cursor.fetchall()
    for count, row in enumerate(orders, 1):
        if count > 9:
            for_dict = {"order_id" : row[0], "customer_name" : row[1], "customer_address" : row[2], "customer_phone" : row[3], "courier_id" : row[4], "status" : row[5],"product_id" : row[6]}
            data_list.append(for_dict)
        else:
            for_dict = {"order_id" : row[0], "customer_name" : row[1], "customer_address" : row[2], "customer_phone" : row[3], "courier_id" : row[4], "status" : row[5],"product_id" : row[6]}
            data_list.append(for_dict)
    cursor.close()
    connection.close()
    return data_list
def add_order_data(name, address, number, courier_id, product_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(
        f"""INSERT INTO orders(customer_name, customer_address, customer_phone, courier_id, status, items)
        VALUES ('{name}', '{address}','{number}', {courier_id}, "preparing", {product_id});"""
                   )
    connection.commit()
    cursor.close()
    connection.close()
def update_order_status(order_id, new_status):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"UPDATE orders set status = '{new_status}' where order_id = {order_id}")
    connection.commit()
    cursor.close()
    connection.close()
def update_order_data(order_id, name, address, number, prod, courier):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM orders where order_id = {order_id}")
    orders = cursor.fetchall()
    for count, row in enumerate(orders, 1):
        for_dict = {
            "order_id" : row[0],
            "customer_name" : row[1],
            "customer_address" : row[2],
            "customer_phone" : row[3],
            "courier_id" : row[4],
            "status" : row[5],
            "product_id" : row[6]}
    if len(name) <= 0:
        name = for_dict["customer_name"]
    if len(address) <= 0:
        address = for_dict["customer_address"]
    if len(number) <= 0:
        number = for_dict["customer_phone"]
    if len(str(prod)) <= 0:
        prod = for_dict["product_id"]
    if len(str(courier)) <= 0:
        courier = for_dict["courier_id"]
    cursor.execute(
        f"""UPDATE orders 
        set customer_name = '{name}', customer_address = '{address}',
        customer_phone = '{number}', items = {prod}, courier_id = {courier}
        WHERE order_id = {order_id}        
        """)
    connection.commit()
    cursor.close()
    connection.close()
def remove_courier_from_order(order_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"UPDATE orders set courier_id = NULL WHERE order_id = {order_id}")
    connection.commit()
    cursor.close()
    connection.close()
def remove_order(order_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM orders WHERE order_id = {order_id}")
    connection.commit()
    cursor.close()
    connection.close()
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")