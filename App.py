from flask import Flask,render_template,send_from_directory
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "C:/download/"

@app.route('/')
def index():
	filename = os.listdir(app.config["UPLOAD_FOLDER"])[0];
	return render_template('download.html',filename=filename)

@app.route('/download/<filename>')
def download(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],filename);


if __name__ == '__main__' :
	app.run()