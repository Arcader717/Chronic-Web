from quart import Quart, redirect, render_template, request

application = Quart(__name__)

@application.route('/')
async def index():
    return "Testing Out AWS"

if __name__ == "__main__":
    import hypercorn
    from hypercorn.asyncio import serve
    from hypercorn.config import config

    config = Config.from_path("hypercorn_config.py")
    serve(application, config)
