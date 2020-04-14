from flask import Blueprint, request
import src.collection.online_entity as online_entity

router = Blueprint(__name__, "router")


@router.route('/', methods=['GET'])
def index():
    return "Hello"

@router.route('/parse', methods = ['GET','POST'])
def parse():
    url = request.args.get('url', None)
    result = online_entity.get_content(url)
    return result
    