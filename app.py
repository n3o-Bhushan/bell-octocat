from flask import Flask, request, json, render_template
import requests

app = Flask(__name__)

@app.route('/octocat')
def helloOcto():
	return "Boom"


if __name__ == '__main__':
	app.run(debug=True)
