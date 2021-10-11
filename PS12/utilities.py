import csv
import sqlite3

def addData(CSVpath):
    conn = sqlite3.connect("CDRdata.db")
    cur = conn.cursor()

    cur.execute(" DROP TABLE IF EXISTS CallData")
    cur.execute("""CREATE TABLE "CallData" (
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
    "roam_nw" TEXT
    )""")

    with open(CSVpath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # print(row) # row is a list, yes yes yes
            calling_number=row[0]
            called_number=row[1]
            date=row[2]
            start_time=row[3]
            end_time=row[4]
            duration=row[5]
            cell1=row[6]
            cell2=row[7]
            cell_type=row[8]
            imei=row[9]
            imsi=row[10]
            smsc=row[11]
            roam_nw=row[12]
            cur.execute("INSERT INTO CallData (calling_number,called_number,date,start_time,end_time,duration,cell1,cell2,cell_type,imei,imsi,smsc,roam_nw) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(calling_number,called_number,date,start_time,end_time,duration,cell1,cell2,cell_type,imei,imsi,smsc,roam_nw))
            conn.commit()

    conn.close()

addData("/home/pi/Desktop/AFKZenCoders/PS12/uploads/CDR1.csv")