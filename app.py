from quart import Quart, redirect, render_template, request

app = Quart(__name__)

@app.route('/')
async def index():
    return "Testing Out AWS"
