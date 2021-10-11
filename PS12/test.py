import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first TEXT,
            last TEXT,
            pay TEXT
            )""")

data = [["dasd","sadsad","yoyo"],["popoipd","iopoipisadsad","pyoyo"]]

for row in data:
    first = row[0]
    last = row[1]
    pay = row[2]

    c.execute("INSERT INTO employees VALUES (?,?,?)",(first,last,pay))
    conn.commit()

conn.close()
