from flask import Blueprint, request, jsonify
from src.preprocessor import preprocessor as preprocessor
import src.collection.online_entity as online_entity
from src.error import ApplicationError, error_list
from aggregator import Aggregator

router = Blueprint(__name__, "router")


@router.route('/', methods=['GET'])
def index():
    return "Hello"

@router.route('/api/url', methods = ['POST'])
def parse_url():
    print("Got request", request.args)
    # No URL found. Raise error
    url = request.args.get('url', None)
    if url is None:
        raise ApplicationError(*error_list["URL_NT_FND"])
    except ApplicationError as error:
        return jsonify(error.to_dict())

    # TODO: Throwing error not added
    news_obj, twitter_obj, error = preprocessor(url, published=True)
    
    if error is not None:
        return jsonify(error.to_dict())
    
    aggregator = Aggregator(news=news_obj, twitter=twitter_obj, published=False)
    aggregator.run_models()

    # TODO: returning result
    return {'response':None}


@router.route('/api/file', methods = ['POST'])
def parse_file():
    print("Got request", request.args)
    fileobj = None
    # If file not found, raise error
    try:
        if 'file' not in request.files:
            raise ApplicationError()
        else:
            fileobj = request.files['file']
    except ApplicationError  as error:
            return jsonify(error.to_dict())

    news_obj, twitter_obj, error = preprocessor(url, published=False)
    
    if error is not None:
        return jsonify(error.to_dict())

    aggregator = Aggregator(news=news_obj, twitter=twitter_obj, published=False)
    aggregator.run_models()

    # TODO: returning result
    return {'response': None}