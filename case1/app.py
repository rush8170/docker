from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	#return '<h1>Flask created</h1>'
	return render_template('prod.html')

#import sys
@app.route('/action',methods = ["POST"])
def product():
	product = request.form['product_name']
	print(product)	
	try:
		fh = open("backup/data.txt","a+")
		fh.write(product+'\n')
		fh.close()
		#print('File created',file=sys.stderr)	
	except IOError:
		print("Error")
	#write code to store in volume storage
	return "Product received:"+product

if __name__=='__main__' :
	app.run(debug=True,host='0.0.0.0')
