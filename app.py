
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

from chronic.common import generate_token

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("main_page.html")

@app.route('/login')
def login():
    return f"{generate_token()}"

