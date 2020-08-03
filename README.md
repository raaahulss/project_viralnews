# Sentiment analysis

The goal of this model is to detect sentence-level political bias for U.S. political news. The logistic regression model achieved an best accuracy of **64.71%**.

## Dataset
* [IBC](https://drive.google.com/open?id=1y0qCANgsCbpDEjeUB660xGHf-z6CLzS5) (2025 liberal sentences, 1701 conservative sentences)

## Models
| Models | Accuracy |
| --- | --- |
| **Logistic regression** | **64.71%** |
| KNN | 54.81% |
| Decision tree | 60.16% |
| Ensemble method | 62.30% |
| RNN | 56.42% |
| RNN + dropout | 58.37% |
| RNN + Word2Vec | 54.54% |
| RNN + Random insertion | 52.67% |
| RNN + Random replacement | 56.68% |
| RNN + Random deletion | 54.54% |
| LSTM | 57.75% |
| BiLSTM | 61.23% |
| Fasttext | 63.72% |
| Fasttext + Data preprocessing | 63.46% |
