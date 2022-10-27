from flask import Flask, render_template, request

# turn this file into a flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

