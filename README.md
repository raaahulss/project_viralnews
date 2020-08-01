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
7. [Future Work](#future-work)
8. [License](#license)
9. [Authors](#authors)

## About
The Carnegie Mellon University (CMU) Master of Information Technology Strategy (MITS) Viral News Project aims to apply machine learning and deep learning techniques to viral news. After the 2016 U.S. presidential election, it became clear that news was no longer just news; it could be manipulated and weaponized by nation states to carry out psychological and information operations against entire populations. Since then, there has a large focus on trying to detect 'fake news' via machine learning and deep learning techniques. One of the more fundamental questions that often doesn't get as much attention is "what makes a news story go viral"? Why do some news stories only get a couple of views, while others are shared thousands of times across social circles? Does it have to do with how long the article is? Does the language of the article affect its virality? Of course, this question has a psychological and human behavior aspect to it, but it can also be attacked from a different angle. What if we could train a neural network to detect whether a certain article will go viral? What if a machine learning model could be trained to pick out the political bias from an article? What is the definition of viral? What if the public's reaction to an article could be capture in one simple chart? These are just some of the questions that we set out to answer as part of this project. In the end, this project only raised more questions than we had before the project started. Nevertheless, there are several contributions that this project makes:

1. A website where users can submit both published and unpublished articles for analysis
2. Three machine learning/deep learning models for predicting article viralness, political bias, and public reaction
3. A custom dataset collected by us which was used for training the viralness model (and the collection methodology, src code, etc.)
4. Extensive documentation for the front end, back end, machine learning models, and everything in between.

Although the goals of this project were quite ambitious and we were time bounded to two semesters, we feel as though we laid the groundwork for individuals and teams to take this work and expand on it. You can read more about ideas for future work in the [Future Work Section](#future-work) 

## How to Use this Repo

This repo consists of multiple different branches. The [master branch](https://github.com/raaahulss/project_viralnews) contains all of the latest production code for the backend and UI. The [production branch](https://github.com/raaahulss/project_viralnews/tree/production) is essentially a copy of the [master branch](https://github.com/raaahulss/project_viralnews), but is linked to our CI/CD pipeline for automatic deployment. The [ui](https://github.com/raaahulss/project_viralnews/tree/ui) and [backend](https://github.com/raaahulss/project_viralnews/tree/backend) branches are where we push our bug fixes and new features before we merge them into the [production branch](https://github.com/raaahulss/project_viralnews/tree/production)

The other three branches [viralness branch](https://github.com/raaahulss/project_viralnews/tree/viralness), [public opinion branch](https://github.com/raaahulss/project_viralnews/tree/public_opinion), and [sentiment analysis branch](https://github.com/raaahulss/project_viralnews/tree/sentiment_analysis) is where we store all of the datasets, notebooks, tests, and documentation for our models. Even though the final deployed models can be seen in the backend code of the [master branch](https://github.com/raaahulss/project_viralnews), the journey that we took to arrive at these final models can be seen in these three branches. 



## Project Overview



## Machine Learning


## UI


## Backend


## Future Work


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
