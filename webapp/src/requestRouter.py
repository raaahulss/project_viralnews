from flask import Blueprint, request
from src.preprocessor import preprocessor as preprocessor
import src.collection.online_entity as online_entity

router = Blueprint(__name__, "router")


@router.route('/', methods=['GET'])
def index():
    return "Hello"

@router.route('/api/url', methods = ['GET','POST'])
def parse():
    print("Got request", request.args)
    url = request.args.get('url', None)
    processed_data = preprocessor(url)
    if url is None:
        return App
    result = online_entity.get_content(url)
    return {'response':result}
