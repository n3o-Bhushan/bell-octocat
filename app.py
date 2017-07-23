from flask import Flask, request, json, render_template
import requests

app = Flask(__name__)

@app.route('/octocat', methods=['GET'])
def helloOcto():
	git = requests.get('https://api.github.com/users/n3o-bhushan/bio')
	print git
	return render_template('index.html', load=git)


@app.route('/')
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
