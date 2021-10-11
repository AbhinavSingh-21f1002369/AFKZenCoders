from flask import Flask, json, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main():
    return 'Homepage'
    
if __name__ == '__main__':
    app.run(host = 0.0.0.0,port = 1313)
