from flask import Flask, send_from_directory


'''Example taken from http://codepen.io/asommer70/blog/serving-a-static-directory-with-flask'''

app = Flask(__name__, static_url_path='/')
app.debug = True

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

if __name__ == "__main__":
				host_loc = "127.0.0.1"
				print "Running server at %s" % host_loc
				app.run(host=host_loc)