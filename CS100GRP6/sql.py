import sqlite3

with sqlite3.connect('munch.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE food")
    c.execute('CREATE TABLE food(cuisines TEXT)')
    c.execute('INSERT INTO food VALUES("Veggie Burger")')
    c.execute('INSERT INTO food VALUES("Cheese Burger")')
    c.execute('INSERT INTO food VALUES("French Fries")')
    c.execute('INSERT INTO food VALUES("Cheeze Pizza")')
    c.execute('INSERT INTO food VALUES("Grilled Chicken Sandwich")')
    c.execute('INSERT INTO food VALUES("Salad Bar")')
    c.execute('INSERT INTO food VALUES("Stir Fry")')
    c.execute('INSERT INTO food VALUES("Banana Cream Pie Pudding Cup")')
    c.execute('INSERT INTO food VALUES("Hot Dog")')
    c.execute('INSERT INTO food VALUES("Braised Beef")')
