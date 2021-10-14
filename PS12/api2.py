from flask import Flask, render_template, request, jsonify,send_file
from werkzeug import secure_filename
import os
import utilities, queries
import logger
app = Flask(__name__)
UPLOAD_FOLDER = '/home/pi/Desktop/AFKZenCoders/PS12/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   logger.logit("Rendered upload.html")
   return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
   uploaded_files = request.files.getlist("file")
   #print(uploaded_files)
   logger.logit(f"/° Multiple Files Upload Start")
   for file in uploaded_files:
      filename = secure_filename(file.filename)
      if filename=="CDR.csv":
         path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
         file.save(path)
         logger.logit("| CDRData Saved")
         utilities.addCDRData(path)
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
      filename = secure_filename(file.filename)
      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      # Saving File
      file.save(path_of_csv)
      logger.logit("CDRData Saved")
      print("CDR File Saved successfully")
      # Loading File To Database
      utilities.addCDRData(path_of_csv)
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
@app.route('/query/1', methods = ['GET'])
def query_1():
   query = "SELECT * FROM CallData ORDER BY duration DESC"
   result = queries.runQuery(query)
   response = {'result':result}
   return jsonify(response)

@app.route('/query/2/', methods = ['GET'])
def query_2():
   # Parsing the Headers
   since = request.args.get('since')
   till = request.args.get('till')
   query = f"SELECT * FROM CallData WHERE start_time < {till} AND start_time > {since};"
   result = queries.runQuery(query)
   response = {'result':result}
   return jsonify(response)

@app.route('/query/3/', methods = ['GET'])
def query_3():
   query = f"SELECT * FROM CallData ORDER BY duration DESC LIMIT 10"
   result = queries.runQuery(query)
   response = {'result':result}
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


if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 1313,debug = True)