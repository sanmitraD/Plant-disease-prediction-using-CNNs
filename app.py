from flask import Flask, render_template, request


app = Flask(__name__)

from inference import get_disease_name



@app.route('/', methods = ['GET','POST'])
def hello():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		if 'file' not in request.files:
			print('file not uploaded')
			return
		file = request.files['file']
		print(request.files)
		image = file.read()
		disease, remidies = get_disease_name(image_bytes=image)
		ind = disease.find('__')
		plant_name = disease[:ind]
		print(plant_name)
		disease_name = disease[ind+2:]
		remidy = remidies['remidy']
		cite = remidies['cite']

		return render_template('result.html',plant= plant_name, disease = disease_name, cite=cite, remidy= remidy)
