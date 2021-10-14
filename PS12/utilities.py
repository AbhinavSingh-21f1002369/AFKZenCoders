import csv
import sqlite3

def convdate(data,time):
  data = data.lower().split("-")
  if len(data[0]) == 1:
    date = "0"+data[0]
  else:
    date = data[0]
  month = data[1]
  year = data[2]
  if month =='jan':
    month = '01'
  elif month =='feb':
    month = '02'
  elif month =='mar':
    month = '03'
  elif month =='apr':
    month = '04'
  elif month =='may':
    month = '05'
  elif month =='jun':
    month = '06'
  elif month =='jul':
    month = '07'
  elif month =='aug':
    month = '08'
  elif month =='sep':
    month = '09'
  elif month =='oct':
    month = '10'
  elif month =='nov':
    month = '11'
  elif month =='dec':
    month = '12'

  time = time.split(":")
  if len(time[0])==1:
      hour = "0" + time[0]
  else:
      hour = time[0]
  minute = time[1]
  second = time[2]
  #print(f"{hour}:{minute}:{second}")

  fstring = f"{year}-{month}-{date} {hour}:{minute}:{second}"
  #print(fstring)
  return(fstring)

def convdur(time):
    time = time.split(":")
    seconds = int(time[0])*60*60 + int(time[1])*60 + int(time[2])
    return seconds

def addThanaData(CSVpath):
    conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
    cur = conn.cursor()

    #cur.execute(" DROP TABLE IF EXISTS CallData")
    cur.execute("""CREATE TABLE IF NOT EXISTS 'Thana' (
    "DISTRICT_ID" INT,
    "THANA_ID" INT,
    "THANA" TEXT
    )""")

    with open(CSVpath) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count+=1
                continue
            #print(row) # row is a list, yes yes yes
            district_id=int(row[0])
            thana_id=int(row[1])
            thana=row[2]
            cur.execute("INSERT INTO Thana (DISTRICT_ID,THANA_ID,THANA) VALUES (?,?,?)",(district_id,thana_id,thana))
            conn.commit()

    conn.close()

def addCDRData(CSVpath):
    conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
    cur = conn.cursor()

    #cur.execute(" DROP TABLE IF EXISTS CallData")
    cur.execute("""CREATE TABLE IF NOT EXISTS 'CallData' (
    "calling_number" TEXT,
    "called_number" TEXT,
    "start_time" DATETIME,
    "end_time" DATETIME,
    "duration" INT,
    "cell1" TEXT,
    "cell2" TEXT,
    "cell_type" TEXT,
    "imei" TEXT,
    "imsi" TEXT,
    "smsc" TEXT,
    "roam_nw" TEXT
    )""")

    with open(CSVpath) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count+=1
                continue
            #print(row) # row is a list, yes yes yes
            calling_number=row[0]
            called_number=row[1]
            date=row[2]
            start_time = convdate(date,row[3])
            #start_time=row[3]
            end_time = convdate(date,row[4])
            #end_time=row[4]
            duration = convdur(row[5])
            print(duration)
            cell1=row[6]
            cell2=row[7]
            cell_type=row[8]
            imei=row[9]
            imsi=row[10]
            smsc=row[11]
            roam_nw=row[12]
            cur.execute("INSERT INTO CallData (calling_number,called_number,start_time,end_time,duration,cell1,cell2,cell_type,imei,imsi,smsc,roam_nw) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(calling_number,called_number,start_time,end_time,duration,cell1,cell2,cell_type,imei,imsi,smsc,roam_nw))
            conn.commit()

    conn.close()

def addBankData(CSVpath):
    conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
    cur = conn.cursor()

    #cur.execute(" DROP TABLE IF EXISTS CallData")
    cur.execute("""CREATE TABLE IF NOT EXISTS 'BankData' (
    "AC_Number" INT,
    "Aadhar_Number" TEXT,
    "Name" TEXT,
    "Bank_Name" TEXT,
    "Mobile_Number" TEXT,
    "Branch_City" TEXT
    )""")

    with open(CSVpath) as csv_file:
        count = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count == 0:
                count+=1
                continue
            #print(row) # row is a list, yes yes yes
            account=row[0]
            aadhar=row[1]
            name=row[2]
            bank_name=row[3]
            mobile_number=row[4]
            branch_city=row[5]

            cur.execute("INSERT INTO BankData (AC_Number, Aadhar_Number, Name, Bank_Name, Mobile_Number, Branch_City) VALUES (?,?,?,?,?,?)",(account, aadhar, name, bank_name, mobile_number, branch_city))
            conn.commit()

    conn.close()

def addCGIData(CSVpath):
    conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 'CGI' (
    "Cell_ID" TEXT,
    "Address" TEXT)
    """)
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
    conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
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
            cur.execute("INSERT INTO FIR (FIR_No,District,Police_Station_ID,Time,Complaint,Act,Section,Mobile_No_of_Complaint) VALUES (?,?,?,?,?,?,?,?)",(FIR_No,District,Police_Station_ID,Time,Complaint,Act,Section,Mobile_No_of_Complaint))
            conn.commit()
    conn.close()

def addthanaListData(CSVpath):
    conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
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
