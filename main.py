from flask import Flask, render_template
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html.jinja')


@app.route('/tail')
def tail():
	# Open log file
	log_path="/opt/Python-tail/app.log"
	# def get_lines_number()
	# def generate_logs()	

	# return flask reponse with generate_logs
	return app.response_class(generate_logs(), mimetype='text/plain')

app.run()
