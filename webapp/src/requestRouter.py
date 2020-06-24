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
    try:
        if url is None:
            raise ApplicationError(*error_list["URL_NT_FND"])
    except ApplicationError as error:
        return return_result(error)

    # TODO: Throwing error not added
    news_obj, twitter_obj, error= preprocessor(url, published=True)
    
    if error is not None:
        return return_result(error)
    
    aggregator = Aggregator(news=news_obj, twitter=twitter_obj, published=False)
    try:
        aggregator.run_models()
    except ApplicationError as error:
        return return_result(error)

    return return_result(error, True,  aggregator, twitter_obj, file_obj)


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
            return return_result(error)

    news_obj, twitter_obj, error = preprocessor(fileobj, published=False)
    
    if error is not None:
        return return_result(error)

    aggregator = Aggregator(news=news_obj, twitter=twitter_obj, published=False)
    try:
        aggregator.run_models()
    raise ApplicationError as error:
        return return_result(error)

    # TODO: returning result
    return return_result(error, False, aggregator, twitter_obj, file_obj)

def return_result(error:ApplicationError, published=None, aggregator=None, tweet=None, file_obj=None):
    if error is not None:
        agg_dict = aggregator.to_dict() if aggregator is not None else None
        file_dict = file_obj.to_dict() if file_obj is not None else None
        tweet_dict = tweet.to_dict() if tweet is not None else None
        input_type = None
        if published:
            input_type = 'Twitter' if tweet is not None else "NonTwitter"
        else:
            input_type = "UnPub"
        return jsonify({
            "input_type" : input_type,
            "models" : agg_dict ,
            "details" : file_dict,
            "metrics" : tweet_dict,
            "error" : ""
        })
    else:
        return jsonify({"error": error.to_dict()})