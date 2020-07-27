from flask import Flask
from src.requestRouter import router, limiter



def main(config="default"):
    app = Flask("IDK")
    app.register_blueprint(router)
    limiter.init_app(app)
    print(__name__, config)
    return app

