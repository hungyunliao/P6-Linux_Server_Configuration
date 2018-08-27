from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "H1111!!!, I love Digital Ocean!"
if __name__ == "__main__":
	app.run()
