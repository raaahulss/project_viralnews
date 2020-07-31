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
The Carnegie Mellon University (CMU) Master of Information Technology Strategy (MITS) Viral News Project aims to apply machine learning and deep learning techniques to viral news. After the 2016 U.S. Presidential election, it became clear that news was no longer just news; it could be manipulated and weaponized by nation states to carry out psychologic and information operations against entire populaces. Since then, there has a large focus on trying to detect 'fake news' via machine learning and deep learning techniques. One of the more fundamental questions that often doesn't get as much attention is "what makes a news story go viral"? Why do some news stories only get a couple of views, while others are shared thousands of times across social circles? Does it have to do with how long the article is? Does the language of the article affect its virality? Of course, this question has a psychological and human behavior aspect to it, but it can also be attacked from a different angle. What if we could train a neural network to detect whether a certain article will go viral? What if a machine learning model could be trained to pick out the political bias from an article? What is the definition of viral? What if the public's reaction to an article could be capture in one simple chart? These are just some of the questions that we set out to answer as part of this project. In the end, this project only raised more questions than we had before the project started. Nevertheless, there are several contributions that this project makes:

1. A website where users can submit both published and unpublished articles for analysis
2. Three machine learning/deep learning models for predicting article viralness, political bias, and public reaction
3. A custom dataset collected by us which was used for training the viralness model (and the collection methodology, src code, etc.)
4. Extensive documentation for the front end, back end, machine learning models, and everything in between.

Although the goals of this project were quite ambitious and we were time bounded to two semesters, we feel as though we laid the groundwork for individuals and teams to take this work and expand on it. You can read more about ideas for future work in the [Future Work Section](#future-work) 

## How to Use this Repo



## Project Overview



## Machine Learning


## UI


## Backend


## Future Work


## License


## Authors

## 

### Software Required
1. Python v3.7.6/Anaconda V4.8.3 [Windows](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe) [MacOS](https://repo.anaconda.com/archive/Anaconda3-2020.02-MacOSX-x86_64.pkg)
2. Node v10.15.3 [All Version](https://nodejs.org/dist/v10.15.3/) 
3. Makefile [Windows](https://sourceforge.net/projects/gnuwin32/) 

### Steps
1. Clone the git repository
2. Run following commands to setup webapp env:
```
conda create -p ./venv python=3.7.6
conda activate ./venv
pip install -r ./webapp/requirements.txt
```
3. Run the following commands to setup ui env:
```
cd ui
npm install
```

### Starting Server

1. For starting backend server:
```
cd webapp
python app.py
```
2. For starting ui server:
```
cd ui
npm start

```

