from src.error import ApplicationError, error_list

def preprocessor(url):
    """
    The preprocessor processes the url and generates appropriate data based on
    the url.
    :error: Returns malformed url error if the url is not a twitter url or one of
    the whitelisted source url 
    """
    fileObj, twitter_metrics, error = None, None, None
    # if user sends a blank or response
    if url is None or url in "":
        error = ApplicationError(*error_list["MAL_URL"])
    embeded_url = None
    if url.startswith("https://twitter.com/"):
        while(True):
            pass
    # code for news media outlet.