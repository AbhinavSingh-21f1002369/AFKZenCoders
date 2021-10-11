from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
import os
import utilities
app = Flask(__name__)
UPLOAD_FOLDER = '/home/pi/Desktop/AFKZenCoders/PS12/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_fxn():
   if request.method == 'POST':
      # Getting the File
      file = request.files['file']
      filename = secure_filename(file.filename)

      # Path for file 
      path_of_csv = os.path.join(app.config['UPLOAD_FOLDER'], filename)

      # Saving File
      file.save(path_of_csv)
      print("File Saved successfully")

      # Loading File To Database
      utilities.addData(path_of_csv)

      return "File Saved and Loaded to Database Successfully"
		
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


if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 1313,debug = True)