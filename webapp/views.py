from webapp import app
from flask import request, render_template



@app.route('/',methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		sourceencoding = request.form['encodings']
		inputtext = request.form['mytext']
		print sourceencoding
		return "Here is your data:%s:%s" %(sourceencoding,inputtext)

