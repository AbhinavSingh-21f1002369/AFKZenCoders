from flask import Flask, render_template, request, jsonify,send_file, redirect
from werkzeug import secure_filename
import os
import utilities, queries
import logger
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
UPLOAD_FOLDER = '/home/pi/Desktop/AFKZenCoders/PS12/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello():
   logger.logit("Rendered root '/'")
   return redirect("http://www.themedallionschool.com/abhinav/PS12/index.html", code=302)

@app.route('/userauth', methods = ['POST','GET'])
def userauth():
   username = request.form.get('username')
   password = request.form.get('password')
   if username=="root" and password=="toor":
      logger.logit(f"Success LOGIN Request Username:{username} Password:{password}")
      return redirect("http://www.themedallionschool.com/abhinav/PS12/upload.html", code=302)
   else:
      logger.logit(f"Failure LOGIN Request Username:{username} Password:{password}")
      return redirect("http://www.themedallionschool.com/abhinav/PS12/incorrect.html", code=302)


@app.route('/upload')
def upload_file():
   logger.logit("Rendered upload.html - test wali")
   return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
   uploaded_files = request.files.getlist("file")
   #number = request.args.get('number')
   #number = "7982345234"
   #print(uploaded_files)
   logger.logit(f"/° Multiple Files Upload Start")
   for file in uploaded_files:
      filename = secure_filename(file.filename)
      if filename=="7982345234.csv":
         path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
         file.save(path)
         number = filename[0:9]
         logger.logit(f"| CDRData Saved {number}")
         utilities.addCDRData(path,number)
      elif filename=="CGI_Dataset.csv":
         path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
         file.save(path)
         logger.logit("| CGIData Saved")
         utilities.addCGIData(path)
      elif filename=="Bank_Details.csv":
         path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
         file.save(path)
         logger.logit("| Bank_Details Saved")
         utilities.addBankData(path)
      elif filename=="FIR_Dataset.csv":
         path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
         file.save(path)
         logger.logit("| FIR_Dataset Saved")
         utilities.addFIRData(path)
      elif filename=="Thana.csv":
         path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
         file.save(path)
         logger.logit("| Thana Saved")
         utilities.addThanaData(path)
      elif filename=="Thana_list_UP.csv":
         path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
         # print(path,file,filename) 
         # /home/pi/Desktop/AFKZenCoders/PS12/uploads/Thana_list_UP.csv <FileStorage: 'Thana_list_UP.csv' ('application/vnd.ms-excel')> Thana_list_UP.csv
         file.save(path)
         logger.logit("| Thana_list_UP Saved")
         utilities.addthanaListData(path)
      else:
         logger.logit(f"File Upload error - {filename}")
   logger.logit(f"\. Multiple Files Uploaded - {len(uploaded_files)}")
   return "OK"
	
@app.route('/uploader/cdr', methods = ['GET', 'POST'])
def upload_cdr_fxn():
   if request.method == 'POST':
      # Getting the File
      file = request.files['file']
      number = request.files['number']
      filename = secure_filename(file.filename)
      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Saving File
      file.save(path_of_csv)
      logger.logit("CDRData Saved")
      print("CDR File Saved successfully")
      # Loading File To Database
      utilities.addCDRData(path_of_csv,number)
      return "CDR File Saved and Loaded to Database Successfully"

@app.route('/uploader/thana', methods = ['GET', 'POST'])
def upload_thana_fxn():
   if request.method == 'POST':
      # Getting the File
      file = request.files['file']
      filename = secure_filename(file.filename)
      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Saving File
      file.save(path_of_csv)
      logger.logit("ThanaData Saved")
      print("Thana File Saved successfully")
      # Loading File To Database
      utilities.addThanaData(path_of_csv)
      return "Thana File Saved and Loaded to Database Successfully"

@app.route('/uploader/bankacc', methods = ['GET', 'POST'])
def upload_bankacc_fxn():
   if request.method == 'POST':
      # Getting the File
      file = request.files['file']
      filename = secure_filename(file.filename)
      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Saving File
      file.save(path_of_csv)
      print("BankAcc File Saved successfully")
      logger.logit("BankData Saved")
      # Loading File To Database
      utilities.addBankData(path_of_csv)
      return "BankAcc File Saved and Loaded to Database Successfully"

@app.route('/uploader/cgi', methods = ['GET', 'POST'])
def upload_cgi_fxn():
   if request.method == 'POST':
      # Getting the File
      file = request.files['file']
      filename = secure_filename(file.filename)
      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Saving File
      file.save(path_of_csv)
      print("CGI File Saved successfully")
      logger.logit("CGIData Saved")
      # Loading File To Database
      utilities.addCGIData(path_of_csv)
      return "CGI File Saved and Loaded to Database Successfully"

@app.route('/uploader/fir', methods = ['GET', 'POST'])
def upload_fir_fxn():
   if request.method == 'POST':
      # Getting the File
      file = request.files['file']
      filename = secure_filename(file.filename)
      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Saving File
      file.save(path_of_csv)
      print("FIR File Saved successfully")
      logger.logit("FIRData Saved")
      # Loading File To Database
      utilities.addFIRData(path_of_csv)
      return "FIR File Saved and Loaded to Database Successfully"

@app.route('/uploader/thanalist', methods = ['GET', 'POST'])
def upload_thanalist_fxn():
   if request.method == 'POST':
      # Getting the File
      file = request.files['file']
      filename = secure_filename(file.filename)
      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Saving File
      file.save(path_of_csv)
      print("Thana List File Saved successfully")
      logger.logit("ThanaListDATA Saved")
      # Loading File To Database
      utilities.addthanaListData(path_of_csv)
      return "Thana File Saved and Loaded to Database Successfully"

# ############################### Queries ##################################
@app.route('/query/1/', methods = ['GET'])
def query_1():
   headers = ["Calling Number","Called Number","Start Time","Duration(sec)","Call Type"]
   query = "SELECT calling_number, called_number, start_time, duration, cell_type FROM CallData ORDER BY duration DESC"
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 1 Call")
   return jsonify(response)

@app.route('/query/2/', methods = ['GET'])
def query_2():
   # Parsing the Headers
   since = str(request.args.get('since')) + " 00:00:00"
   till = str(request.args.get('till')) + " 23:59:59"
   headers = ["Calling Number","Called Number","Start Time","End Time","Duration(sec)","Start Tower","End Tower","Call Type","IMEI","IMSI","SMSC","Service Provider"]
   query = f'SELECT * FROM CallData WHERE start_time < "{till}" AND start_time > "{since}";'
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   fString = f">>> Query 2 Call since:{since}, till:{till}"
   logger.logit(fString)
   return jsonify(response)

@app.route('/query/3/', methods = ['GET'])
def query_3():
   headers = ["Calling Number","Called Number","Start Time","End Time","Duration(sec)","Start Tower","End Tower","Call Type","IMEI","IMSI","SMSC","Service Provider"]
   query = f"SELECT * FROM CallData ORDER BY duration DESC LIMIT 10"
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 3 Call")
   return jsonify(response)

@app.route('/query/4/', methods = ['GET'])
def query_4():
   headers = ["Dialled Number","Total Dialled Calls","Total Duration"]
   query = f'''SELECT called_number, count(*) as 'Frequency', sum(duration) as 'Total Duration' from CallData where cell_type="OUT" GROUP by called_number ORDER by Frequency DESC'''
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 4 Call")
   return jsonify(response)

@app.route('/query/5/', methods = ['GET'])
def query_5():
   headers = ["Caller","Total Recieved Calls","Total Duration"]
   query = f'''SELECT calling_number, count(*) as 'Frequency', sum(duration) as 'Total Duration' from CallData where cell_type="IN" GROUP by calling_number ORDER by Frequency DESC'''
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 5 Call")
   return jsonify(response)

@app.route('/query/6/', methods = ['GET'])
def query_6():
   headers = ["Called Number","Total Duration(sec)"]
   query = f"SELECT DISTINCT called_number, sum(duration) as totalDuration FROM CallData WHERE called_number NOT in (7982345234) GROUP BY called_number  ORDER BY totalDuration DESC "
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 6 Call")
   return jsonify(response)

@app.route('/query/7/', methods = ['GET'])
def query_7():
   headers = ["Called Number","Duration","Call Type"]
   query = f'SELECT called_number, duration, cell_type FROM CallData WHERE cell_type="OUT" ORDER by duration DESC'
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 7 Call")
   return jsonify(response)

@app.route('/query/8/', methods = ['GET'])
def query_8():
   headers = ["Calling Number","Duration","Call Type"]
   query = f'SELECT calling_number, duration, cell_type FROM CallData WHERE cell_type="IN" ORDER by duration DESC'
   result = queries.runQuery(query)
   headers = ["Phone NO","Duration","Call Type"]
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 8 Call")
   return jsonify(response)

@app.route('/query/9/', methods = ['GET'])
def query_9():
   headers = ["Calling Number","Called Number","Start Time","End Time","Duration(sec)","Start Tower","End Tower","Call Type","IMEI","IMSI","SMSC","Service Provider"]
   # Parsing the Headers
   date = request.args.get('date')
   query = f'SELECT * from CallData where start_time like "{date}%" or end_time like "{date}%"'
   result = queries.runQuery(query)
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   fString = f">>> Query 10 Call date:{date}"
   logger.logit(fString)
   return jsonify(response)

@app.route('/query/10/', methods = ['GET'])
def query_10():
   headers = ["Start Time","End Time","Tower 1","Tower 2"]
   # Parsing the Headers
   date = request.args.get('date')
   query = f'''SELECT start_time, end_time, cell1, cell2 from CallData where (start_time like "2021-01-04%" or end_time like "2021-01-04%")'''
   result = queries.runQuery(query)
   #print(result)
   fString = f">>> Query 10 Call date:{date}"
   
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(fString)
   return jsonify(response)

@app.route('/query/11/', methods = ['GET'])
def query_11():
   query = f'''SELECT DISTINCT called_number FROM CallData WHERE cell_type="OUT" UNION SELECT DISTINCT calling_number FROM CallData WHERE cell_type="IN"'''
   result = queries.runQuery(query)
   #print(result)
   #res = []
   #for item in result:
   #   res.append(item[0])
   headers = ["Mobile Number"]
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   logger.logit(">>> Query 11 Call")
   return jsonify(response)


@app.route('/query/12/', methods = ['GET'])
def query_12():
   # Parsing the Headers
   number = request.args.get('number')
   query = f'''SELECT * FROM CallData WHERE called_number="{number}" or calling_number="{number}"'''
   result = queries.runQuery(query)
   headers = ["Calling Number","Called Number","Start Time","End Time","Duration(sec)","Start Tower","End Tower","Call Type","IMEI","IMSI","SMSC","Service Provider"]
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   fString = f">>> Query 12 Call number:{number}"
   logger.logit(fString)
   return jsonify(response)

@app.route('/query/20/', methods = ['GET'])
def query_20():
   # Parsing the Headers
   fir = request.args.get('fir')
   query = f'SELECT * from FIR WHERE FIR_No={int(fir)}'
   result = queries.runQuery(query)
   #print(result)
   headers = ["FIR No","District","PS ID","Time of FIR","Complainant","Act","Section","Complainant Mobile Number"]
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   fString = f">>> Query 20 Call for:{fir}"
   logger.logit(fString)
   return jsonify(response)

@app.route('/loadedfiles', methods = ['GET'])
def loadedfiles():
   csv_files = []
   for filename in os.listdir("/home/pi/Desktop/AFKZenCoders/PS12/uploads/"):
      if filename.endswith(".csv"):
         csv_files.append(filename)
   logger.logit("Rendered upload.html")
   return jsonify({'CSV files':csv_files})

@app.route('/deleteloaded', methods = ['GET'])
def deleteloaded():
   csv_files = []
   for filename in os.listdir("/home/pi/Desktop/AFKZenCoders/PS12/uploads/"):
      if filename.endswith(".csv"):
         fstring = f"/home/pi/Desktop/AFKZenCoders/PS12/uploads/{filename}"
         os.remove(fstring)
   os.remove("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
   logger.logit("### Files Deleted ###")
   return jsonify({'CSV files':csv_files})

# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
   logger.logit("Rendered download.html")
   return render_template('download.html',value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = "/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db"
    logger.logit("Database Downloaded")
    return send_file(file_path, as_attachment=True, attachment_filename='')

@app.route('/logs')
def logs():
   with open("/home/pi/Desktop/AFKZenCoders/PS12/Logs.txt","r") as f:
      lines = f.readlines()
      f.close()
   formated_lines = []
   for i in range(len(lines)-1,0,-1):
      formated_lines.append(lines[i])

   return jsonify({'logs':formated_lines})

@app.route('/graph')
def graph():
   query = f'SELECT date,in_count,out_count,sms_count,total from "798234523"'
   result = queries.runQuery(query)
   #print(result)
   headers = ["Date","Incomming Calls","OutGoing Calls","SMS","Total Interactions"]
   if len(result) != 0:
      response = {'headers':headers,'rows':result}
   else:
      response = {'headers':["No Data Available"],'rows':[]}
   fString = f">>> GRAPH Call"
   logger.logit(fString)
   return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 1313,debug = True)
