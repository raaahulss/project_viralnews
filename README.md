# Project IDK

## Setup

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
python main.py
```
2. For starting ui server:
```
cd ui
npm start
```