import sqlite3

def add_product():
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn = sqlite3.connect('webshop.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")
    conn.close()

def my_quit():
    pass

menu = {1:("Quit", "my_quit"),
        2:("Add Product", "add_product")}

#5
def set_stock():
    product_id = input('product_id: ')
    new_stock = input('new stock: ')
    conn = sqlite3.connect('webshop.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET stock = ? WHERE product_id = ?', (new_stock, product_id,))
    print(cursor.fetchall())
    conn.close()

menu[4] = ("Change stock of item", "set_stock")

#6
def show_receipt():
    order_id = input('order_id: ')
    conn = sqlite3.connect('webshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT p.name, oi.quantity * oi.unit_price FROM order_items oi JOIN orders o ON o.order_id = oi.order_id JOIN products p ON p.product_id = oi.product_id WHERE oi.order_id = ?', (order_id,))
    result = cursor.fetchall()
    for item, price in result:
        print(f"{item:<20} {price:>8.2f} SEK")
    conn.close()

menu[5] = ("Show an order's receipt", "show_receipt")

#7
'''
ValueError: could not convert string to float: 'abc'
'''
def add_product():
    try:
        name = input("Name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except Exception as e:
        print(e)
        return
    conn = sqlite3.connect('webshop.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")
    conn.close()

#8
def best_selling():
    conn = sqlite3.connect('webshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT p.name, SUM(oi.quantity) FROM products p JOIN order_items oi ON oi.product_id = p.product_id GROUP BY oi.product_id ORDER BY SUM(oi.quantity) DESC LIMIT 3')
    for name, quantity in cursor.fetchall():
        print(f"{name:<20} {quantity:>4}")
    conn.close()

menu[6] = ("Top 3 best-selling products", "best_selling")

def main():
    choice = None
    while (choice != 1):
        for key, value in sorted(menu.items()):
            print(f'{key} {value[0]}')
        try:
            choice = int(input())
            if not choice in menu.keys():
                choice = None
                raise(ValueError)
        except Exception as e:
            print(e)
        chosen = menu[choice][1]
        globals()[chosen]()

main()
