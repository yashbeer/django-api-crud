## Coding Challenge By Fynd

Create a RESTful API for movies(something similar to IMDB). For this we would like you to use:

1. MySql or SQLlite to store data
2. Any Python Framework for implementing the APIs

There need to be 2 levels of access:

1. admin = who can add, remove or edit movies.
2. users = who can just view the movies.

● There should also be a decent implementation to search for movies

● Document your code well so that we can test the API with ease

● For your convenience I have attached some data that you can use to populate your database

● Try and deploy this on Heroku. Ensure that you parse the JSON file and ingest it into the application deployed on Heroku

● Once deployed suppose this application became very famous and started to receive a ton of traffic. Your application now contains metadata about 5M movies and receives 15M API hits per day both from anonymous as well as authenticated users. Suggest an architecture to scale up this system to 5x of these specs. You can also think of potential bottlenecks at all layers of the stack and how will you solve for these.

● Make your design decisions wisely, you will be asked questions on the implementation at the end of the task

-----------------

## Solution

Database Used: Postgresql
Python Framework: Django Rest Framework (DRF)

## API Documentation

`[GET] /api/movies/`

Response:
```
[
    {
        "id": 3,
        "name": "Star Wars",
        "director": "George Lucas",
        "popularity": 88.8,
        "imdb_score": 8.8,
        "genre": [
            {
                "name": "Action"
            },
            {
                "name": "Adventure"
            },
            {
                "name": "Fantasy"
            },
            {
                "name": "Sci-Fi"
            }
        ]
    },
    .
    .
    .
    {
        "id": 8,
        "name": "Star Trek",
        "director": "Marc Daniels",
        "popularity": 86.0,
        "imdb_score": 8.6,
        "genre": [
            {
                "name": "Adventure"
            },
            {
                "name": "Sci-Fi"
            }
        ]
    }
]
```

