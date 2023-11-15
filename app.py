from quart import Quart, redirect, render_template, request

app = Quart(__name__)

@app.route('/')
async def index():
    return "Testing Out AWS"

if __name__ == "__main__":
    import hypercorn
    from hypercorn.asyncio import serve
    from hypercorn.config import config

    config = Config.from_path("hypercorn_config.py")
    serve(app, config)