from webapp import app
from flask import request, render_template
import json
from flask import jsonify



@app.route('/',methods=['GET'])
def index():
	"""
	endpointurl : '/'
	allowed methods : 'GET'
	required params : none
	functionality : reads two text files and adds options to list 
	response_data : renders index.html with tamil and english options supported
	"""
	tamiloptions_lst = []
	englishoptions_lst = []
	with open('webapp/tamiloptions.txt','r')as f:
		for item in f.readlines():
			tamiloptions_lst.append(item.strip().decode('utf-8'))
	with open('webapp/englishoptions.txt','r')as f:
		for item in f.readlines():
			englishoptions_lst.append(item.strip().decode('utf-8'))
	return render_template('index.html', data=tamiloptions_lst, engdata=englishoptions_lst)


@app.route('/convert', methods=['GET'])
def doconvert():
	"""
	endpointurl : '/convert'
	allowed methods : 'GET'
	required params : encodings, input_data
	functionality : converts to destination encode
	response_data : returns converted data

	(e.x) /convert
	      'encodings': 'boomi',
	      'mytext': 'this is boomi encode input'
	"""
	response_data = {}
	response_data['encodings'] = request.args.get('encodings')
	response_data['input_data'] = request.args.get('mytext')
	return jsonify(response_data)

