from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/')
app.debug = True

@app.route('/')
def send_index():
				return send_from_directory('static/static_html', 'helloworld.html')

if __name__ == "__main__":
				host_loc = "127.0.0.1"
				print "Running server at %s" % host_loc
				app.run(host=host_loc)