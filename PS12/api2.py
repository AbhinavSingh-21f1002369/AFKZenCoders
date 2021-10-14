from flask import Flask, render_template, request, jsonify,send_file
from werkzeug import secure_filename
import os
import utilities, queries
app = Flask(__name__)
UPLOAD_FOLDER = '/home/pi/Desktop/AFKZenCoders/PS12/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
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
   query = f"SELECT * FROM CallData WHERE start_time > {till} AND start_time < {since};"
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
   return jsonify({'CSV files':csv_files})

@app.route('/deleteloaded', methods = ['GET'])
def deleteloaded():
   csv_files = []
   for filename in os.listdir("/home/pi/Desktop/AFKZenCoders/PS12/uploads/"):
      if filename.endswith(".csv"):
         fstring = f"/home/pi/Desktop/AFKZenCoders/PS12/uploads/{filename}"
         os.remove(fstring)
   os.remove("/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db")
   return jsonify({'CSV files':csv_files})

# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)


@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = "/home/pi/Desktop/AFKZenCoders/PS12/CDRdata.db"
    #print(file_path)
    return send_file(file_path, as_attachment=True, attachment_filename='')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 1313,debug = True)