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

@app.route('/specific/<int:b_id>',methods = ['GET'])
def specific(b_id):
	with sqlite3.connect('books.db') as conn:
		cur = conn.cursor()
		sql = 'SELECT * FROM BOOK WHERE ID ='+str(b_id)
		cur.execute(sql)
		row = cur.fetchone()
	return render_template('specific.html',row=row)


@app.route('/delete/<int:b_id>',methods = ['GET','POST'])
def delete(b_id):
	if request.method == 'POST':
		with sqlite3.connect('books.db') as conn:
			cur = conn.cursor()
			sql = 'DELETE FROM BOOK WHERE ID ='+str(b_id)
			cur.execute(sql)
		return redirect(url_for('jobs'))
	return render_template('delete.html',b_id = b_id)

@app.route('/addrecord',methods=['GET','POST'])
def addrecord():
	if request.method == 'POST':
		try:
			with sqlite3.connect('books.db') as conn:
				cur = conn.cursor()
				b_id = int(request.form['id'])
				b_name = request.form['b_name']
				b_author =request.form['b_author']
				year = int(request.form['b_year'])
				isbn = int(request.form['b_isbn'])

				v = str((b_id,b_name,b_author,year,isbn))
				sql = "INSERT INTO BOOK VALUES " + v
				cur.execute(sql)
				conn.commit()
			return redirect(url_for('jobs'))
		except:
			return redirect(url_for('jobs'))
	return render_template('addrecord.html')

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
