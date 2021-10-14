# AFKZenCoders
AFKZenCoders
 
 ## PS12
 ----
 API endpoints
 
- [loaded files](http://iot.ccnet.in:1313/loadedfiles) - displayes the loaded in the DataBase files (CDRs)
- [upload](http://iot.ccnet.in:1313/upload) - upload a CSV (CDR) file here and python will add it to the CDR database
- [multi-upload](https://themedallionschool.com/abhinav/PS12/test.html) - Upload multiple files here
> Upload CSV in [this Format](https://github.com/AbhinavSingh-21f1002369/AFKZenCoders/blob/main/PS12/static/CDR1.csv)
- [delete loaded](http://iot.ccnet.in:1313/deleteload) - deletes the CSV files in the uploads folder and also deletes the database
- [download db](http://iot.ccnet.in:1313/downloadfile/PS12Database.db) - downloads the db file


Sample Queries
[Query](http://iot.ccnet.in/query/1) - `SELECT * FROM CallData ORDER BY duration DESC`
[Query 2](http://iot.ccnet.in:1313/query/2?since='2021-01-01 16:56:04'&till='2021-01-02 13:28:02') - `SELECT * FROM CallData WHERE start_time < '2021-01-04 11:23:54' AND start_time > '2021-01-03 21:14:00';`
[Query 3](http://iot.ccnet.in/query/3) - `SELECT * FROM CallData ORDER BY duration DESC LIMIT 10`
