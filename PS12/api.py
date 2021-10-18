import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template


UPLOAD_FOLDER = '/home/pi/Desktop/AFKZenCoders/PS12/uploads/'

#app = Flask(__name__)
app = Flask(__name__, template_folder='/home/pi/Desktop/AFKZenCoders/PS12/templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Upload API
@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("File Saved successfully")
      #send file name as parameter to downlad
            #return redirect('/downloadfile/'+ filename)
            return "File Saved Successfully"
    return render_template('upload_file.html')


# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)


@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename
    print(file_path)
    return send_file(file_path, as_attachment=True, attachment_filename='')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 1313,debug = True)