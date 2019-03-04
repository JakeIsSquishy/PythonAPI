import markdown
import os
import shelve

#Import the framework
from flask import Flask, g

# Create an instance of Flask
app = Flask(__name__)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = shelve.open("devices.db")
	return db

@app.teardown_appcontext
def teardown_dby(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

@app.route("/")
def index():
	"""Present some documentation"""

	# Open the README file
	with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
		
		# Read the content of the file
		content = markdown_file.read()

		# Convert to HTML
		return markdown.markdown(content)
