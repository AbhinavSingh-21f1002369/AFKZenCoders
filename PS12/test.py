import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS `testTable` (
    "calling_number" TEXT,
    "called_number" TEXT,
    "date" TEXT,
    "start_time" TEXT,
    "end_time" TEXT,
    "duration" TEXT,
    "cell1" TEXT,
    "cell2" TEXT,
    "cell_type" TEXT,
    "imei" TEXT,
    "imsi" TEXT,
    "smsc" TEXT,
    "roam_nw" TEXT,
    "test" TEXT
    )""")
conn.commit()
conn.close()
"""for row in data:
    first = row[0]
    last = row[1]
    pay = row[2]

    c.execute("INSERT INTO employees VALUES (?,?,?)",(first,last,pay))
    conn.commit()

conn.close()
"""