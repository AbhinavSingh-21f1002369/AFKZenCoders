import requests
import sqlite3

payload = {'date':"2021-01-04"}

r = requests.get("http://iot.ccnet.in:1313/query/10/",params = payload)

logs= r.json()['result']
conn = sqlite3.connect("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
cur = conn.cursor()

response = []
location = ""

[t1,t2,l1,l2]
[t3,t4,l3,l1]
[t5,t2,l1,l3]

for i in range(0,len(logs)):
    #print(log)
    log = logs[i]
    time1 = log[0]
    time2 = log[1]
    id1 = log[2]
    if location == "":
        location = log[2]
    if log[3] != log[2]:
        location = log[3]
        cur.execute(f'SELECT Address FROM CGI where Cell_ID="{location}"')
        record1 = cur.fetchall()
        if len(record1) != 1:
            response.append(log[1],"Unknown Location")
        else:
            response.append([log[1],record1[0]])
        continue
    if location != log[2]:







    if len(record1)!=1:
        record1.append("Location Not Known")
    id2 = log[3]
    response.append([time1,record1])
    cur.execute(f'SELECT Address FROM CGI where Cell_ID="{id2}"')
    record2 = cur.fetchall()
    if len(record2)!=1:
        record2.append("Location Not Known")
    response.append([time2,record2])
print(type(response),len(response))
    #print(record1,record2)

conn.close()

"""

out = [['2021-01-04 16:32:03', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 16:42:34', []]]
[['2021-01-04 16:32:03', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 16:42:34', []], ['2021-01-04 18:42:25', []], ['2021-01-04 19:01:09', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]]]
[['2021-01-04 16:32:03', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 16:42:34', []], ['2021-01-04 18:42:25', []], ['2021-01-04 19:01:09', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 20:23:12', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 20:23:12', []]]
[['2021-01-04 16:32:03', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 16:42:34', []], ['2021-01-04 18:42:25', []], ['2021-01-04 19:01:09', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 20:23:12', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 20:23:12', []], ['2021-01-04 20:51:41', [('Fawn Brake Avenue, Husainganj, Lucknow, Uttar Pradesh 226001, India',)]], ['2021-01-04 21:11:03', [('D/3, GaneshGanj Rd, Raj Bhavan Colony, Aminabad, Lucknow, Uttar Pradesh 226001, India',)]]]

print(len(out))"""