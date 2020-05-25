import flask
from flask import render_template,request,jsonify,redirect,url_for
import sqlite3


app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
	ufasasfsafsers = ['Rishabh','Sumit','Vishal']
	allblogs = {
		'Rishabh':['Food','Programming'],
		'Sumit':['Clothes','Animals'],
		'Vishal':['PubG','Whatsapp'],
		'Test':['Testing','Done']
	}
	return render_template("testing.html", users = ufasasfsafsers,
		allblogs = allblogs)


@app.route('/blogs')
def blogs():
	allblogs = {
		'Rishabh':['Food','Programming'],
		'Sumit':['Clothes','Animals'],
		'Vishal':['PubG','Whatsapp']
	}
	return render_template('blogs.html', allblogs = allblogs)

@app.route('/jobs')
def jobs():

	with sqlite3.connect('books.db') as conn:
		cur = conn.cursor()
		sql = 'SELECT TITLE,AUTHOR,YEAR,ID FROM BOOK'
		cur.execute(sql)
		rows = cur.fetchall()
	return render_template('jobs.html',rows = rows)


@app.route('/api/v1/checkprime')
def check_prime():
	if 'num' in request.args:
		n = int(request.args['num'])
	else:
		return "No 'num' provided"
	result = {"Number":n}
	for i in range(2,n//2+1):
		if n%i == 0:
			result['isprime']=False
			break
	else:
		result['isprime']=True

	return jsonify(result)
if __name__ == "__main__":
	app.run()
