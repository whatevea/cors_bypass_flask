from flask import Flask,Response,request,jsonify
import requests
app=Flask(__name__)
@app.route('/')
def homepage():
	if request.args.get('url') is None:
		return "This is the homepage please add url parameter and replace the & with ^ character"
	else:
		url=request.args['url'].replace("^","&")
		content=requests.get(url)
		try:
			content=content.json()
			response=jsonify(content)
		except:
			content=content.text
			response=jsonify({"content":content})
		response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
		response.headers.add('Access-Control-Allow-Origin', '*')
		response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
		return response
