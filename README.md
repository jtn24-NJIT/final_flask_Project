Hello, my name is Jake Tyler Nhan. I am a fourth year NJIT student, majoring in a Bachelor's degree in Computer Science. This is the repo for the fourth and final project of IS 218, SEC. 004 of Spring 2022. In this project, there is a simple login system that also allows for uploading of csv transaction files.

# Project Setup

[![Production Workflow 1](https://github.com/jtn24-NJIT/final_flask_Project/actions/workflows/prod.yml/badge.svg?branch=master)](https://github.com/jtn24-NJIT/final_flask_Project/actions/workflows/prod.yml)

* [Production Deployment](https://jtn24-final-proj-prod.herokuapp.com/)


[![Development Workflow 3.8](https://github.com/jtn24-NJIT/final_flask_Project/actions/workflows/dev.yml/badge.svg?branch=master)](https://github.com/jtn24-NJIT/final_flask_Project/actions/workflows/dev.yml)

* [Developmental Deployment](https://jtn24-final-proj-dev.herokuapp.com/)


## Setting up CI/CD

The result of this will be that when you create a pull request to merge a branch to master, it will deploy to your
heroku development app/dyno and when you merge or push to master on github, it will deploy the app to the production heroku
app/dyno.

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest
