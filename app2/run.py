import sqlite3
from flask import Flask, jsonify, send_from_directory, g, request
from time import time

'''Example taken from http://codepen.io/asommer70/blog/serving-a-static-directory-with-flask'''
app = Flask(__name__, static_url_path='/')
app.debug = True

'''DATABASE setup'''
DATABASE = '/data/data_1.db'

def connect_to_database():
	return sqlite3.connect('data/data_1.db')

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = connect_to_database()
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def insert_message(message):
	insert_q = "INSERT INTO messages (time, message) VALUES (?,?)"
	con = get_db()
	cur = con.cursor()
	cur.execute(insert_q, (time(), message))
	con.commit()
	return "message was successfully entered"

def get_messages():
	select_q = "SELECT * FROM messages"
	cur = get_db().cursor()
	cur.execute(select_q)
	rows = cur.fetchall()
	return rows


@app.route('/')
def send_index():
	return send_from_directory('static/static_html', 'index.html')

@app.route('/<path:path>')
def send_static_html(path):
	return send_from_directory('static/static_html', path)

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('static/css', path)

@app.route('/data', methods=['GET', 'POST'])
def data_request():
	if request.method == 'POST':
		message = request.get_json().get('message_to_insert', None)
		print "message was %s" % message
		if message != None:
			print "this got called"
			success = insert_message(message)
			return jsonify(success=success)
		else:
			return "message was None"
	else:
		return "was not POST"

@app.route('/get_data', methods=['POST'])
def serve_data():
	if request.method == 'POST':
		messages = get_messages()
		return jsonify({"messages" : messages})

if __name__ == "__main__":
	host_loc = "127.0.0.1"
	print "Running server at %s" % host_loc
	app.run(host=host_loc)