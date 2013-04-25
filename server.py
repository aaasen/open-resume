
import requests
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users/<username>')
def get_user(username):
    return requests.get('https://api.github.com/users/%s' % (username)).text

if __name__ == '__main__':
    app.run(debug=True)
