import processing
import os
import fnmatch
from flask import Flask, Response, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory,jsonify
from werkzeug import secure_filename
import shelve
import socket
import re
from flask.ext.assets import Environment, Bundle

ALLOWED_EXTENSIONS = set(['pdf','PDF'])

app = Flask(__name__)

# configure assets
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('css/main.scss', 'css/base.scss', filters='pyscss', output='css/all.css')
homescss = Bundle('css/main.scss', 'css/homepage.scss', filters='pyscss', output='css/home.css')
readscss = Bundle('css/main.scss', 'css/reader.scss', filters='pyscss', output='css/read.css')
assets.register('scss_all', scss)
assets.register('scss_home', homescss)
assets.register('scss_read', readscss)



## set upload folder
app.config['UPLOAD_FOLDER'] = './pdfproject/static/uploads'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
def findFile(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

@app.route("/")
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
			print (os.path.join(app.config['UPLOAD_FOLDER'], filename))
			ratio = processing.process(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print ratio
			print "ran?"
			return redirect(url_for('uploaded_file', filename=filename, ratio=ratio)) #"upload success" #redirect(url_for('uploaded_file',filename=filename))
		return "No!"
	return "NO"

@app.route('/uploads/<filename>/<ratio>')
def uploaded_file(filename, ratio):
	p = filename+'.*jpg$'
	patt = re.compile(p)
	result = []
	print ratio
	n=1
	for file in os.listdir("./pdfproject/static/uploads"):
		if patt.match(file):
			result.append("static/uploads/"+filename+str(n)+'.jpg')
			n = n+1
	jsondata = "/static/uploads/"+filename+".json.txt"
	return render_template('processed.html',result=result, ratio=ratio,jsondata=jsondata)#send_from_directory(app.config['UPLOAD_FOLDER'], filename)
