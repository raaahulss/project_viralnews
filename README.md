# Viralness Model

## Original Goal

Our original goal was to try to predict if a given article will go viral or not with an accuracy of at leasy 60%. We started by doing an extensive literature review and found that most work in this area has used the [UCI News Popularity Data Set](https://archive.ics.uci.edu/ml/datasets/Online+News+Popularity). As we started working with this data, we found that this data (collected from Mashable) will not extrapolate well to other news articles. So we set out on a mission to collect our own [data](https://github.com/raaahulss/project_viralnews/blob/viralness/data/viralness_dataset.csv)(note the pipe '|' seperator using our own [method](https://github.com/raaahulss/project_viralnews/tree/viralness/dataset).

## New Goal

Once we had our new data, we ran into a new issue: what does 'viral' in the context of news articles even mean? And so with that, we decided to leave that question up to social scientists and use the number of retweets an article gets as our virality metric. With that we laid out a couple different problm statements, but ended up going with a multi-class classification based on a log 10 scale of retweets (0-10 retweets, 11-100, retweets, 101-1000 retweets, 1000+ retweets). Of course this is not ideal. We originally wantd to implement a regression model to try to predict exactly how many retweets an article would get, but due to time constraints, we had to settle for the multi-class classification model. 

## Model experimentation

We tested a bunch of different kinds of models using all both text and metadata features ([standard machine learning models](https://github.com/raaahulss/project_viralnews/tree/viralness/model/Baseline), [RNNs](https://github.com/raaahulss/project_viralnews/tree/viralness/model/RNN), [LSTMs](https://github.com/raaahulss/project_viralnews/tree/viralness/model/LSTM)). We found that models trained on the text of an article (content + title) performed the best, and that LSTMs (specifcally Bi-LSTMS) did the best. The notebook for the final deployed model can be found [here](https://github.com/raaahulss/project_viralnews/blob/viralness/model/final/lstm_glove_final_DEPLOYMENT.ipynb), and the weights, vocab2index, vocab, can be found in the [final](https://github.com/raaahulss/project_viralnews/tree/viralness/model/final) directory. The final model has an overall accuracy of around 60%, and has a F1 for class_3 (1000+ retweets) of 32%. The reason that our deployed model has a worse accuracy than the final model seen in the (#Model Results) section is because after deploying our model, we continued to work on tuning some hyper parrameters, but did not have time to deploy the final model into production.  

## Model Results

Here are some results from various model runs just to give an idea of how various models perform on different types of features and class distributions:

### Metadata Features


#### Regression (# of tweets) 

| Model | RMSE |
|:-----:|:------:|
|Linear regression | 647.84| 

#### Binary Classification  (threshold=median)

| Model | Overall Accuracy|
|:-----:|:-----:|
|RNN |61%|

#### Multi-class Classification (quantiles) 

| Model | Overall Accuracy|
|:-----:|:--------:|
RNN | 39%
KNN | 42%
Decision Tree|  43%
Xgboost | 43%
SVM |45%
Random Forest | 50%

#### Multi-class Classification (log base 10) using Metadata Features

| Model | Overall Accuracy |
|:-------:|:---------:|
 RNN |58%*
Decision Tree | 63%*
KNN | 69%*
SVM | 71%*
Random Forest | 71%*
Xgboost|  71%*

*Large class imbalance; predicts majority class

### Text Features

#### Multi-class classification (log base 10) tf-idf (content + title)


| Model | Overall Accuracy|
|:-------:|:------------------:|
|Random Forest  | 41%*     |
|Naive Bayes |  46%*|
|Linear SVC | 49%* |
|Linear Regression | 50%* |

*Large class imbalance; predicts majority class

#### Multi-class classification (log base 10) (content + title, no stop words)

| Model | Balance Technique | Overall Accuracy |class_3 F1 |
|:-------:|:-----------------:|:--------------:|:---------:|
LSTM | Weighted Random Sampling | 32% | 7%
LSTM + GloVe | Weighted Random Sampling | 31% | 3%
BiLSTM + GloVe | Weighted Random Sampling | 64% | 10%
BiLSTM + GloVe | Synonym Replacement | 63% | 43%











