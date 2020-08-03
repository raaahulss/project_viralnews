Datasets:


Sentiment140 dataset with 1.6 million tweets (negative, neutral and positive)
https://www.kaggle.com/kazanova/sentiment140#training.1600000.processed.noemoticon.csv


Methodology:


Assumption: A particular news article has also been tweeted by the official twitter handle of the news agency (Most of the big new agencies do, verified for a few articles in Washington Post and New York Times)

Use twitter search API to fetch the tweet and the comments on that tweet
Upto 7-day old article - Free on Standard
Upto 30-day old article
Free on sandbox
$149 on Premium
Full archive
Free on sandbox
$99 on Premium

Analyze the article and the comments to extract features. Use some kind of similarity score to report the sentiment


Machine Learning:


Analysing the twitter comments to produce classes - (Binary classification(Agree/Disagree) 


References:


Source https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90
