#Personal data lab
import sqlite3
conn = sqlite3.connect('webshop.db')
cursor = conn.cursor()

#1
cursor.execute('SELECT first_name, last_name, city FROM customers')
for first_name, last_name, city in cursor.fetchall():
    print(f'{first_name} {last_name} {city}')

#2
max_price = input('Max price: ')
cursor.execute('SELECT name, price FROM products WHERE price < ?', (max_price,))
for name, price in cursor.fetchall():
    print(f'{name} {price}')

#3
category = input('Category: ')
cursor.execute('SELECT COUNT(product_id) FROM products WHERE category = ?', (category,))
print(*(cursor.fetchone()))

#4
'''
If any part of the fstring is made up of user input, then the user can input any string there
including one that starts a whole other query or command that can basically be any SQL command.
By using the ? approach we are guaranteed that whatever goes into the ? is just a variable and not
a seperate command in itself, thus the command will only do what we intended it to do.
'''

conn.close()