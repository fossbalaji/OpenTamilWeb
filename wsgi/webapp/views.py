# -*- coding: utf-8 -*-
from webapp import app
from flask import request, render_template
import json
from flask import jsonify
from tamil.txt2unicode import encode2unicode as e2u
from utils import d



@app.route('/',methods=['GET'])
def index():
	"""
	endpointurl : '/'
	allowed methods : 'GET'
	required params : none
	functionality : reads two text files and adds options to list 
	response_data : renders index.html with tamil and english options supported
	"""
	# tamiloptions_lst = []
	# englishoptions_lst = []
	# with app.open_resource('tamiloptions.txt','r')as f:
	# 	for item in f.readlines():
	# 		tamiloptions_lst.append(item.strip().decode('utf-8'))
	# with app.open_resource('englishoptions.txt','r')as f:
	# 	for item in f.readlines():
	# 		englishoptions_lst.append(item.strip())
	# master_di = []
	# for tam,eng in zip(tamiloptions_lst, englishoptions_lst):
	# 	master_di.append((eng,tam))
	# print "****", master_di
	master_di= dict([(k.decode('utf-8'), v) for k, v in d.items()])
	return render_template('index.html', data=master_di)


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
	user_encoding = request.args.get('encodings')
	#print type(request.args.get('mytext'))
	input_data = request.args.get('mytext')
	temp_en = user_encoding.lower()
	if temp_en.startswith('auto'):
		response_data['result_unicode']= e2u.auto2unicode(input_data.encode('utf-8'))
	else:
		temp_en += '2utf8'
		get_charmap = e2u._all_encodes_[temp_en]
		response_data['result_unicode'] = e2u.encode2unicode(input_data.encode('utf-8'), get_charmap)
	return jsonify(response_data)

## Testing url
@app.route('/test', methods=['GET'])
def test():
	return "Testing page works"
