#from flask import Flask, render_template
from time import sleep

#app = Flask(__name__)

#@app.route('/')
def index():
	return render_template('index.html.jinja')

# Utile pour l'export sur site internet
""" il s'agit de la syntaxe pour créer une page sur le site flask """
#@app.route('/tail')
def tail():
	# log file
	log_path="/opt/Python-tail/app.log"
	
	# BONUS : def get_lines_number()
		# Dans cette fonction il faut réussir à trouver le nombre de ligne du fichier et retourner ce nombre
	# def generate_logs()	
		# Fonction qui lit un fichier en temps réel: ouvrir le fichier, boucler en permanence sur les lignes et les afficher.
		# Utilisez yield plutot que return
		
	# return flask reponse with generate_logs
	#return app.response_class(generate_logs(), mimetype='text/plain')

# Permet de lancer l'application Flask
#app.run()
