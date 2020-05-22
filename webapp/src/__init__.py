from flask import Flask
from src.requestRouter import router

def main(config="default"):
    app = Flask("IDK")
    app.register_blueprint(router)
    print(__name__, config)
    return app