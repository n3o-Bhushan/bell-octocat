from flask import Flask, request, json, render_template
import requests

app = Flask(__name__)

@app.route('/octocat')
def helloOcto():
	git = requests.get('https://api.github.com/users/octocat/orgs')
	return render_template(index.html, load=json.dump(git))


@app.route('/')
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
