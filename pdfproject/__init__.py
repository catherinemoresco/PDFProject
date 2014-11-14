#import automate
import os
from flask import Flask, Response, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory,jsonify
from werkzeug import secure_filename
import shelve
import socket
UPLOAD_FOLDER = './pdfproject/uploads'
ALLOWED_EXTENSIONS = set(['pdf','PDF'])

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = 'PDFProject/pdfproject/uploads'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
	return render_template("layout.html")

@app.route("/start/")
def homeprint():
	return render_template("start.html")

@app.route("/process/",methods=['GET','POST'])
def upload_file():
	print 'upload file'
	try:
		os.stat(app.config['UPLOAD_FOLDER'])
	except:
		os.mkdir(app.config['UPLOAD_FOLDER'])
	if request.method == 'POST':
		file = request.files['uploadFile']
		print type(file.stream)
		print 'filename' + file.filename
		if file and allowed_file(file.filename):
			print 'allowing file'
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print "saved?"
			return redirect(url_for('uploaded_file', filename=filename)) #"upload success" #redirect(url_for('uploaded_file',filename=filename))
		return "No!"
	return "NO"	

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
