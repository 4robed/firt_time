from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/index')
def index():
	user = {'username': 'Hung'}
	return render_template('index.html', title = 'Home', user =user)