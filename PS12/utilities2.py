def addCGIData(CSVpath):
    conn = sqlite3.connect("CDRdata.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 'CGI' (
    "Cell_ID" TEXT,
    "Address" TEXT,
    )""")
    with open(CSVpath) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count+=1
                continue
            #print(row) # row is a list, yes yes yes
            Cell_ID=row[0]
            Address=row[1]
            cur.execute("INSERT INTO CGI (Cell_ID,Address) VALUES (?,?)",(Cell_ID,Address))
            conn.commit()
    conn.close()

def addFIRData(CSVpath):
    conn = sqlite3.connect("CDRdata.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 'FIR' (
    "FIR_No" INT,
    "District" TEXT,
    "Police_Station_ID" INT,
    "Time" DATETIME,
    "Complaint" TEXT,
    "Act" TEXT,
    "Section" TEXT,
    "Mobile_No_of_Complaint" TEXT
    )""")
    with open(CSVpath) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count+=1
                continue
            #print(row) # row is a list, yes yes yes
            FIR_No=row[0]
            District=row[1]
            Police_Station_ID=row[2]
            Time= convdate(row[3],row[4])
            Complaint=row[5]
            Act=row[6]
            Section=row[7]
            Mobile_No_of_Complaint=row[8]
            cur.execute("INSERT INTO FBI (FIR_No,District,Police_Station_ID,Time,Complaint,Act,Section,Mobile_No_of_Complaint) VALUES (?,?,?,?,?,?,?,?)",(FIR_No,District,Police_Station_ID,Time,Complaint,Act,Section,Mobile_No_of_Complaint))
            conn.commit()
    conn.close()

def addthanaListData(CSVpath):
    conn = sqlite3.connect("CDRdata.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 'ThanaList' (
    "District_ID" INT,
    "District" INT,
    "State" TEXT
    )""")
    with open(CSVpath) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count+=1
                continue
            #print(row) # row is a list, yes yes yes
            District_ID=row[0]
            District=row[1]
            State=row[2]
            cur.execute("INSERT INTO ThanaList (District_ID,District,State) VALUES (?,?,?)",(District_ID,District,State))
            conn.commit()
    conn.close()