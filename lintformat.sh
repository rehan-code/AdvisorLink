#!/usr/bin/env bash

# Installation steps for flask server
cd server
find . -type f -name "*.py" | xargs flake8 
find . -type f -name "*.py" | xargs  black
# Installation steps for react
cd ../web
find . -type f -name "*.py" | xargs flake8
find . -type f -name "*.py" | xargs  black

#The ‘find’ finds all files that end with the specific as stated above ‘.py’ 
#and passes the args for flake8 to be run on ach individual file