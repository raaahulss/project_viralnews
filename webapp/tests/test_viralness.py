from src.models.viralness import get_viralness
from src.collection.news_fetcher import get_news_from_url

def test_if_valid_result():
    test  = get_news_from_url("https://www.nytimes.com/2020/07/03/us/politics/trump-coronavirus-mount-rushmore.html")
    result = get_viralness(test[0])
    print(result)
    assert result != None
