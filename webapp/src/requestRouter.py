from flask import Blueprint, request
import src.collection.online_entity as online_entity

router = Blueprint(__name__, "router")


@router.route('/', methods=['GET'])
def index():
    return "Hello"

@router.route('/parse', methods = ['GET','POST'])
def parse():
    print("Got request", request.args)
    url = request.args.get('url', None)
    if url is None:
        return "null"
    result = online_entity.get_content(url)
    return {'response':result}
    