import pymysql
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	#return '<h1>Flask created</h1>'
	return render_template('prod.html')

#import sys
@app.route('/action',methods = ["POST"])
def product():
	username = request.form['username']
	password = request.form['password']
	print(username,password)
	import pymysql

	# Open database connection
	db = pymysql.connect("172.17.0.2","root","qwerty","db" )
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	try:
	   # Execute the SQL command
	   cursor.execute("INSERT INTO login(username,pass) VALUES(\'"+username+"\',\'"+password+"\')") 
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# disconnect from server
	db.close()	
	#write code to store in volume storage
	return "Request received:"+username+" "+password

if __name__=='__main__' :
	app.run(debug=True,host='0.0.0.0')
