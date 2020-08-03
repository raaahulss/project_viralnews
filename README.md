<div align="center">

# CMU MITS Viral News Project

</div>

## Table of Contents
1. [About](#about)
2. [How to Use this Repo](#how-to-use-this-repo)
3. [Project Overview](#project-overview)
4. [Machine Learning](#machine-learning)
5. [UI](#ui)
6. [Backend](#backend)
7. [Deployment](#deployment)
8. [Future Work](#future-work)
9. [License](#license)
10. [Authors](#authors)

## About
The Carnegie Mellon University (CMU) Master of Information Technology Strategy (MITS) Viral News Project aims to apply machine learning and deep learning techniques to viral news. After the 2016 U.S. presidential election, it became clear that news was no longer just news; it could be manipulated and weaponized by nation states to carry out psychological and information operations against entire populations. Since then, there has been a large focus on trying to detect 'fake news' via machine learning and deep learning techniques. One of the more fundamental questions that often doesn't get as much attention is "what makes a news story go viral"? Why do some news stories only get a couple of views, while others are shared thousands of times across social circles? Does it have to do with how long the article is? Does the language of the article affect its virality? Of course, this question has a psychological and human behavior aspect to it, but it can also be attacked from a different angle. What if we could train a neural network to detect whether a certain article will go viral? What if a machine learning model could be trained to pick out the political bias from an article? What is the definition of viral? What if the public's reaction to an article could be captured in one simple chart? These are just some of the questions that we set out to answer as part of this project. In the end, this project only raised more questions than we had before the project started. Nevertheless, there are several contributions that this project makes:

1. A website where users can submit both published and unpublished articles for analysis.
2. Three machine learning/deep learning models for predicting article viralness, political bias, and public reaction.
3. A custom dataset collected by us which was used for training the viralness model (and the collection methodology, src code, etc.).
4. Documentation for the front end, back end, machine learning models, and everything in between.

Although the goals of this project were quite ambitious and we were time bounded to two semesters, we feel as though we laid the groundwork for individuals and teams to take this work and expand on it. You can read more about ideas for future work in the [Future Work Section](#future-work) 

## How to Use this Repo

This repo consists of multiple different branches. The [master branch](https://github.com/raaahulss/project_viralnews) contains all of the latest production code for the backend and UI. The [production branch](https://github.com/raaahulss/project_viralnews/tree/production) is essentially a copy of the [master branch](https://github.com/raaahulss/project_viralnews), but is linked to our CI/CD pipeline for automatic deployment. The [ui](https://github.com/raaahulss/project_viralnews/tree/ui) and [backend](https://github.com/raaahulss/project_viralnews/tree/backend) branches are where we push our bug fixes and new features before we merge them into the [production branch](https://github.com/raaahulss/project_viralnews/tree/production)

The other three branches [viralness branch](https://github.com/raaahulss/project_viralnews/tree/viralness), [public opinion branch](https://github.com/raaahulss/project_viralnews/tree/public_opinion), and [sentiment analysis branch](https://github.com/raaahulss/project_viralnews/tree/sentiment_analysis) is where we store all of the datasets, notebooks, tests, and documentation for our models. Even though the final deployed models can be seen in the backend code of the [master branch](https://github.com/raaahulss/project_viralnews), the journey that we took to arrive at these final models can be seen in these three branches. 



## Project Overview

This project is meant to provide a user-friendly website that anyone can use to analyze news articles. The front end is implemented using ReactJS framework, while the backend is implemented using Flask. The deep learning models use PyTorch and TensorFlow. The website allows for user input via a web browser, and the backend provides a callable API as well. Whenever a published article is submitted by a user, the content and metadata for the article are scraped. If it is a news article from Twitter, then the replies to the tweet are also fetched using Twitter's 30-day search API. Once the backend has all of this data for an article, each model is run and the output for each is displayed on a dashboard to the user. 



## Machine Learning

Each model has its own branch, and more detailed information can be found about each one on its respective branch. Here is a quick overview of each model:
1. [viralness model](https://github.com/raaahulss/project_viralnews/tree/viralness): The viralness model is a multi-class text classification Bi-LSTM w/ GloVe embeddings model implemented using PyTorch. The model was trained on a [dataset](https://github.com/raaahulss/project_viralnews/blob/viralness/data/retweet_July_20_20_19.csv) that we collected over the span of about a month (~38,000 articles) using our own [approach](https://github.com/raaahulss/project_viralnews/tree/viralness/dataset_collector). The model is entirely trained on only the content and title of an article, so it can be used on both published and unpublished articles. The model predicts how many retweets an article will get using a log base 10 scale (0-10 retweets, 11-100 retweets, 101-1000 retweets, 1000+ retweets). The final accuracy of the deployed model is around 60%. If you would like a copy of the cleaned and hydrated dataset with the articles already scraped, please contact either [Sam Teplov](https://github.com/samteplov) or [Gaurav Deshpande](https://github.com/g2des)

2. [political bias model](https://github.com/raaahulss/project_viralnews/tree/sentiment_analysis): The political bias model is a logistic regression model which can detect the political bias in an article. It was trained on the IBC dataset which consists of sentences that are labeled liberal, conservative, or neutral. The final accuracy of the deployed model is around 64%. 

3. [public opinion model](https://github.com/raaahulss/project_viralnews/tree/public_opinion): The public opinion model is a deep learning model implemented using TensorFlow which analyzes the reactions to an article on Twitter. It runs each reaction through the model and then averages the overall sentiment detected in all of the responses. The final accuracy of the deployed model is around 83%. 

## UI

The [ui](https://github.com/raaahulss/project_viralnews/tree/master/ui) is implemented using ReactJS framework. It currently only provides support for web browsers and was not developed for mobile devices. To start the UI, simply run the following commands from the [ui](https://github.com/raaahulss/project_viralnews/tree/master/ui) directory:

```
npm install
npm start
```

In order to build the UI to serve it statically, simply run the following command from the [ui](https://github.com/raaahulss/project_viralnews/tree/master/ui) directory:

```
npm build
```

## Backend

The backend is implemented using the Python framework Flask. In order to run the backend server, navigate to the [webapp](https://github.com/raaahulss/project_viralnews/tree/master/webapp) directory and run the following commands:

```
conda create -p ./venv python=3.7.6
conda activate ./venv
pip install -r ./webapp/requirements.txt
python -m nltk.downloader stopwords
python -m spacy download en_core_web_sm
python app.py
```
In addition, for our implementation, the weights and vocabs for each model were stored in S3 and pulled when the server started up. This code can easily be modified to accommodate local weight and vocab files.  

## Deployment

If you would like to deploy the webapp, you can follow a similar configuration to us. In the [deployment](https://github.com/raaahulss/project_viralnews/tree/ui/deployment/backend) directory, there are a couple of files that will help you. First, you will need nginx, as well as gunicorn (or you can use something else). The [deployment](https://github.com/raaahulss/project_viralnews/tree/ui/deployment/backend) directory contains the unit file for running the web application as a systemd service, as well as the nginx configuration file used. We also used [CertBot](https://certbot.eff.org/) to get SSL/TLS setup. 

## Future Work

In terms of future work, there are a number of different aspects of this project that can be improved and worked on:
1. Collecting a bigger dataset for the viralness model
2. Improving the performance of the viralness model
3. Collecting a bigger dataset for the political bias model
4. Improving the accuracy of the political bias model
5. Adding new models (fake news detection) 
6. Improving the UI to support mobile devices
7. Creating a mobile app

The possibilities of this project are endless and there is still a lot of work to be done. 


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/raaahulss/project_viralnews/blob/master/LICENSE) file for details


## Authors

- [Gaurav Deshpande](https://github.com/g2des):
  - [Backend](https://github.com/raaahulss/project_viralnews/tree/master/webapp) Developer
  - [Viralness model](https://github.com/raaahulss/project_viralnews/tree/viralness) Researcher & Developer
- [Fangzhou Xie](https://github.com/fangzhouxie):
  - [Backend](https://github.com/raaahulss/project_viralnews/tree/master/webapp) Developer
  - [Political bias model](https://github.com/raaahulss/project_viralnews/tree/sentiment_analysis) Researcher & Developer
- [Rahul Salla](https://github.com/raaahulss):
  - [UI](https://github.com/raaahulss/project_viralnews/tree/master/ui) Developer 
  - [Public opinion model](https://github.com/raaahulss/project_viralnews/tree/public_opinion) Researcher & Developer
- [Sam Teplov](https://github.com/samteplov):
  - [UI](https://github.com/raaahulss/project_viralnews/tree/master/ui) Developer
  - [Viralness model](https://github.com/raaahulss/project_viralnews/tree/viralness) Researcher & Developer
