import processing
import os
import fnmatch
from flask import Flask, Response, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory,jsonify
from werkzeug import secure_filename
import shelve
import socket
import re
from flask.ext.assets import Environment, Bundle
import datetime

ALLOWED_EXTENSIONS = set(['pdf','PDF'])

app = Flask(__name__)

## Configure assets
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('css/main.scss', 'css/base.scss', filters='pyscss', output='css/all.css')
homescss = Bundle('css/main.scss', 'css/homepage.scss', filters='pyscss', output='css/home.css')
readscss = Bundle('css/main.scss', 'css/reader.scss', filters='pyscss', output='css/read.css')
assets.register('scss_all', scss)
assets.register('scss_home', homescss)
assets.register('scss_read', readscss)



## Set upload folder to static/uploads
app.config['UPLOAD_FOLDER'] = './pdfproject/static/uploads'

def allowed_file(filename):
	""" Takes a filename, and makes sure that it has an allowed extension. Returns True if allowed, False if disallowed. """
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def findFile(pattern, path):
	""" Taking a pattern and a path, return list of filenames in given path that match pattern. """
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result

@app.route("/")
def homeprint():
	""" Render homepage """ 
	return render_template("start.html")

@app.route("/process/",methods=['GET','POST'])
def upload_file():
	""" Upload and process file """
	print 'upload file'
	## Check for existence of specified upload folder, and create one if it does not exist.
	try:
		os.stat(app.config['UPLOAD_FOLDER'])
	except:
		os.mkdir(app.config['UPLOAD_FOLDER'])
	## Upload file.
	if request.method == 'POST':
		file = request.files['uploadFile']
		print type(file.stream)
		print 'filename' + file.filename
		if file and allowed_file(file.filename):
			print 'allowing file'
			## Secure filename to prevent malicious inputs
			filename = secure_filename(file.filename + str(datetime.datetime.utcnow()))
			## Save file
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print "saved?"
			print (os.path.join(app.config['UPLOAD_FOLDER'], filename))
			## Run image processing modules, which write processed images to upload folder.
			processing.process(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print "ran?"
			## Redirect to reading view
			return redirect(url_for('uploaded_file', filename=filename)) #"upload success" #redirect(url_for('uploaded_file',filename=filename))
		return "No!"
	return "No file uploaded. Please try again."

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	""" Display uploaded file """
	## Create pattern
	p = filename+'.*jpg$'
	patt = re.compile(p)
	## Iterate through uploads directory to find filenames that match pattern
	## Accumulate results in list
	result = []
	n=1
	for file in os.listdir("./pdfproject/static/uploads"):
		if patt.match(file):
			result.append("static/uploads/"+filename+str(n)+'.jpg')
			n = n+1
	## Read stored JSON data from file
	jsondata = "/static/uploads/"+filename+".json.txt"
	## Render reading pages
	return render_template('processed.html',result=result, jsondata=jsondata)#send_from_directory(app.config['UPLOAD_FOLDER'], filename)
