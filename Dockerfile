# use an official python runtime as a parent image
FROM python:3.7

# set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1

# ensure that console output looks familiar 
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /umbrella_app

# set the working directory
WORKDIR /umbrella_app

# install dependencies
RUN pip install pipenv

# COPY ./Pipfile /home/gersain/programming/planes/Pipfile
COPY ./Pipfile /umbrella_app

# install dependences
RUN pipenv install --system --skip-lock

# Copy project
COPY . /umbrella_app