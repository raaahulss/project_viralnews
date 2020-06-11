import pytest
from src.preprocessor import *

@pytest.mark.parametrize("url, target",
[
("https://twitter.com","twitter"),
("https://www.nytimes.com/","nytimes"),
("https://www.washingtonpost.com/","washingtonpost"),
])
def test_given_valid_url_returns_true(url, target):
    """
    given a url from a whitelisted source and is valid
    then returns the domain for the passed url
    """
    result = is_whitelisted_url(url)
    assert result == target


@pytest.mark.parametrize("url, target",
[
("https://www.wsj.com/articles/george-floyd-the-athlete-classmate-remembered-at-houston-school-11591714153?mod=hp_lead_pos1",
 "George Floyd, the Athlete and Classmate, Is Remembered at Houston Funeral"),
("https://www.nytimes.com/2020/06/09/us/politics/republicans-police-reform.html?action=click&module=Top%20Stories&pgtype=Homepage",
 "G.O.P. Scrambles to Respond to Public Demands for Police Overhaul"),
("https://www.cnn.com/2020/06/09/politics/trump-supporters-florida/index.html",
 "A world away from Washington, loyal supporters stand by the President in Trump country"),
])
def test_fetch_news_from_valid_url(url, target):
    """
    given a valid url, fetch the news article from the website
    """
    news, _, _ = preprocessor(url, True)
    assert news.title == target


@pytest.mark.parametrize("url, target",
[
("sdjfakjdshf", "Application Error MAL_URL : Invalid Request URL."),
("https://abcnews.go.com/Health/ominous-sign-arizona-sees-bounce-back-covid-19/story?id=71154842&cid=clicksource_4380645_2_heads_hero_live_hero_hed","Application Error UNSUP_SRC : The provided url is not supported."),
("https://www.npr.org/2020/06/11/872856822/thousands-of-workers-say-their-jobs-are-unsafe-as-economy-reopens","Application Error UNSUP_SRC : The provided url is not supported."),
])
def test_fetch_news_from_invalid_url(url, target):
    """
    given a valid url, fetch the news article from the website
    """
    _, _, error = preprocessor(url, True)
    assert str(error) == target
