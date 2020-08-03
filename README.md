# Goal:
Given a tweet, classify the opinion being conveyed by the author


# Problem:
Binary Classification (agree or disagree)


# Dataset:
[Sentiment140 dataset with 1.6 million tweets](https://www.kaggle.com/kazanova/sentiment140#training.1600000.processed.noemoticon.csv)


# Assumption:
- A particular news article given by the user has been tweeted by the official twitter handle of the news agency.
- Use twitter search API to fetch the tweet, its comments and retweets.


# Approach:
- Clean, explore, and visualize the dataset
- Feature extraction using count vectorization, tf-idf, n-gram model, word2vec, and doc2vec
- Implement and compare range of machine learning models
- Implement neural networks with feature extractions
- Tune the hyperparameters to improve model performance


# Results:

- Baseline Models

| Models                 |  Accuracy  |
|:----------------------:|:----------:|
|  Zero Rule Classifier  |   50.39%   |
|    TextBlob Library    |   60.82%   |

- Simple ML Models

|                   Models                  | Accuracy |
|:-----------------------------------------:|:--------:|
|                 Linear SVC                |  79.73%  |
|          Multinomial Naive Bayes          |  77.47%  |
|           Bernoulli Naive Bayes           |  78.35%  |
|              Ridge Classifier             |  79.58%  |
|                  AdaBoost                 |  73.26%  |
|                 Perceptron                |  75.93%  |
|             Passive Aggressive            |  71.47%  |
|            Ensemble (LR+SVC+RC)           |  79.79%  |
| Count Vectorization + Logistic Regression |  79.92%  |
|        Tf-Idf + Logistic Regression       |  80.26%  |

- Neural Networks

|                  Models                  | Accuracy |
|:----------------------------------------:|:--------:|
|        Artificial Neural Networks        |  81.54%  |
|               NN + Word2Vec              |  80.47%  |
|               NN + Doc2Vec               |  72.51%  |
| CNN + Word2Vec (Bigram+Trigram+Fourgram) |  83.18%  |


# [References](https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90)
