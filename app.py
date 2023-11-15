
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main_page.html")

@app.route('/login')
def login():
    return "Hi, this page is still a work in progress"

