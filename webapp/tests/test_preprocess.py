import pytest
from src.preprocessor import *

@pytest.mark.parametrize("url, target",
[
("https://twitter.com","twitter"),
("twitter.com","twitter"),
("https://www.nytimes.com/","nytimes"),
("www.nytimes.com/","nytimes"),
("https://www.washingtonpost.com/","washingtonpost"),
("www.washingtonpost.com/","washingtonpost"),
])
def test_given_valid_url_returns_true(url, target):
    """
    given a url from a whitelisted source and is valid
    then returns the domain for the passed url
    """
    result = is_whitelisted_url(url)
    assert result == target