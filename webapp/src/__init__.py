from flask import Flask
from src.requestRouter import router, limiter


def main():
    app = Flask("IDK")
    app.register_blueprint(router)
    limiter.init_app(app)
    print(__name__)
    return app
