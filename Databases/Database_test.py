import sqlite3
import PyQt5

con = sqlite3.connect('customer.db')

cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE customers (first_name text, last_name text, email text)''')

many_customers = [
                    ("Tim", "Müller", "!"),
                    ("Jakob", "Fischer", "OOO")]


#cur.execute("""UPDATE customers SET last_name = 'Mueller'
    #WHERE rowid == 3
    #""")

#cur.execute("DELETE from customers WHERE rowid == 3")
#cur.execute("INSERT INTO customers VALUES(?, ?, ?)", ("Jakob", "Mueller", "com"))

#con.commit()

# Insert a row of data
#cur.executemany("INSERT INTO customers VALUES(?, ?, ?)", many_customers)
cur.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

items = cur.fetchall()
for item in items:
    print(item)


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

