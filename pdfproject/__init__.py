import processing, extract
import os
import time
import datetime
import fnmatch
from flask import Flask, Response, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory,jsonify
from werkzeug import secure_filename
import shelve
import socket
import re
from flask.ext.assets import Environment, Bundle
from apscheduler.schedulers.background import BackgroundScheduler

ALLOWED_EXTENSIONS = set(['pdf','PDF'])

app = Flask(__name__)

## Configure assets
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('css/main.scss', 'css/base.scss', filters='pyscss', output='css/all.css')
homescss = Bundle('css/main.scss', 'css/homepage.scss', filters='pyscss', output='css/home.css')
readscss = Bundle('css/main.scss', 'css/reader.scss', filters='pyscss', output='css/read.css')
rotatescss = Bundle('css/main.scss', 'css/rotate.scss', filters='pyscss', output='css/rotate.css')
assets.register('scss_all', scss)
assets.register('scss_home', homescss)
assets.register('scss_read', readscss)
assets.register('scss_rotate', rotatescss)


## Maximum Time To Keep Files in Seconds
maxTime = 10800
removalInterval = int(round(maxTime/60))
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

##Automatically remove files after specified max time
sched = BackgroundScheduler();
@sched.scheduled_job('interval',minutes=removalInterval)
def timed_removal():
	print("Removal Time")
	currentTime = datetime.datetime.now();
	for file in os.listdir("./pdfproject/static/uploads"):
		pathToFile = "./pdfproject/static/uploads/"+file
		timeCreated = datetime.datetime.fromtimestamp(os.path.getctime(pathToFile)) 
		timePassed = currentTime-timeCreated;
		if (timePassed>datetime.timedelta(seconds=maxTime)):
			print(currentTime)
			print(pathToFile)
			os.remove(pathToFile)
sched.start()
@app.route("/")
def homeprint():
	""" Render homepage """ 
	return render_template("start.html")

@app.route("/upload/", methods=['GET','POST'])
def upload():
	"""Upload file and allow user to orient page"""
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
			## Get and save image thumbnails
			extract.getThumbnailImage(app.config['UPLOAD_FOLDER'],filename)
			return redirect(url_for('rotate', filename=filename)) #"upload success" 
			print filename
		return "No!"
	return "No file uploaded. Please try again."


@app.route("/rotate/<filename>")
def rotate(filename):
	thumb = "/static/uploads/" +  filename +  "thumb.jpeg"
	print thumb
	return render_template('rotate.html', thumb=thumb, filename=filename)


@app.route("/process/<filename>", methods=['GET', 'POST'])
def process_file(filename):
	""" Upload and process file """
	if request.method=='POST':
		try:
			rotate_angle = int(request.form['rotateby'])
			if rotate_angle**2 > 16:
				rotate_angle = (rotate_angle % 4)
			rotate_angle = rotate_angle * 90
		except:
			rotate_angle = 0
	processing.process(os.path.join(app.config['UPLOAD_FOLDER'], filename), rotate_angle)
	print "ran?"
	## Redirect to reading view
	return redirect(url_for('uploaded_file', filename=filename)) #"upload success" #redirect(url_for('uploaded_file',filename=filename))

@app.route('/upload/<filename>')
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
