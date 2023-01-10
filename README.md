# Ad Manager API

## Introduction

This service is a small API of Ad Manager based on Google's Ad Manager

### Main features

* Full CRUD restful API for single objects for:
  * Ad unit
  * Line item
  * Creative
* Filter line items with 0 to 5 keywords that pass as query parameters.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:itamar27/AdManagerAPI.git
    $ cd AdManagerAPI

#### Make sure that your docker app is running on your machine
    
Run this command in the terminal:

    $ docker-compose up -d --build
    
    
Then simply apply the migrations:

    $ docker-compose exec web python manage.py migrate --noinput
    

You can now run the development server:

    $ docker-compose up -d