import sqlite3

def runQuery(query):
    conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    conn.close()
    return records

if __name__ == "__main__":
    print(runQuery("SELECT Name, Aadhar_Number, AC_Number from BankData BD, FIR F WHERE BD.Mobile_Number=F.Mobile_No_of_Complaint"))