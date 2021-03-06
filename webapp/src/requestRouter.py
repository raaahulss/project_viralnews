from src.preprocessor import preprocessor as preprocessor
from src.error import ApplicationError, error_list
from src.aggregator import Aggregator
from src.constants import MIN_CONTENT_LEN

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import io
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

router = Blueprint(__name__, "router")
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["2000 per day", "500 per hour"]
)


@router.route('/', methods=['GET'])
@cross_origin()
def index():
    return "Hello"


@router.errorhandler(429)
@cross_origin()
def ratelimit_handler(e):
    return return_result(ApplicationError(*error_list["RATE_LIMIT_EXCEEDED"]))


@router.route('/api/url', methods=['POST'])
@limiter.limit('60/minute')
@cross_origin()
def parse_url():
    print("Got request", request.args)
    # No URL found. Raise error
    url = request.args.get('url', None)
    print(url)
    try:
        if url is None:
            raise ApplicationError(*error_list["URL_NT_FND"])
    except ApplicationError as error:
        return return_result(error)

    # TODO: Throwing error not added
    news_obj, twitter_obj, error = preprocessor(url, published=True)
    
    if error is not None:
        return return_result(error)
    if len(news_obj.content.split(' ')) < MIN_CONTENT_LEN:
        return return_result(ApplicationError(*error_list["CONTENT_TOO_SHORT"]))

    aggregator = Aggregator(news=news_obj, tweet=twitter_obj, is_twitter=twitter_obj is not None)
    try:
        aggregator.run_models()
    except ApplicationError as error:
        return return_result(error)

    return return_result(error, True,  aggregator, twitter_obj, news_obj)


@router.route('/api/file', methods=['POST'])
@limiter.limit('60/minute')
@cross_origin()
def parse_file():
    print("Got request", request.args)

    # If file not found, raise error
    try:
        if 'file' not in request.files:
            raise ApplicationError(*error_list["FILE_NT_FND"])
        else:
            filest = request.files['file']
            if not filest.filename.endswith('doc') and not filest.filename.endswith('docx'):
                raise ApplicationError(*error_list["FILE_NT_SUP"])
            else:
                file_obj = io.BytesIO(filest.read())
    except ApplicationError as error:
        return return_result(error)

    news_obj, twitter_obj, error = preprocessor(file_obj, published=False)
    
    if error is not None:
        return return_result(error)
    if len(news_obj.content.split(' ')) < MIN_CONTENT_LEN:
        return return_result(ApplicationError(*error_list["CONTENT_TOO_SHORT"]))

    aggregator = Aggregator(news=news_obj, tweet=twitter_obj, is_twitter=False)
    try:
        aggregator.run_models()
    except ApplicationError as error:
        return return_result(error)

    # TODO: returning result
    return return_result(error, False, aggregator, twitter_obj, news_obj)


def return_result(error: ApplicationError, published=None, aggregator=None, tweet=None, news_obj=None):
    if error is None:
        agg_dict = aggregator.to_dict() if aggregator is not None else None
        news_dict = news_obj.to_dict() if news_obj is not None else None
        tweet_dict = tweet.to_dict() if tweet is not None else None
        if published:
            input_type = 'Twitter' if tweet is not None else "NonTwitter"
        else:
            input_type = "UnPub"
        return jsonify({
            "input_type": input_type,
            "models": agg_dict,
            "details": news_dict,
            "metrics": tweet_dict,
            "error": ""
        })
    else:
        return jsonify({"error": error.to_dict()})
