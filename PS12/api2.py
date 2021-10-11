from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/home/pi/Desktop/AFKZenCoders/PS12/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_fxn():
   if request.method == 'POST':
      file = request.files['file']
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print("File Saved successfully")
      return "File Saved Successfully"
		
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 1313,debug = True)