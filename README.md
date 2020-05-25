## Usecase

### Create a RESTful API for movies (something similar to IMDB).

Stack to be used:
1. Django for implementing the APIs
2. Mysql as database

There need to be 2 levels of access:

1. admin = who can add, remove or edit movies.
2. users = who can just view the movies.

There should also be a decent implementation to search for movies.

Once deployed suppose this application became very famous and started to receive a ton of traffic. Your application now contains metadata about 5M movies and receives 15M API hits per day both from anonymous as well as authenticated users. Suggest an architecture to scale up this system to 5x of these specs. You can also think of potential bottlenecks at all layers of the stack and how will you solve for these.

-----------------

# Implementation

https://fyndyashbeer.herokuapp.com/api/movies/

Database Used: Postgresql

Python Framework: Django Rest Framework (DRF)

# API Documentation

### 1. List of Movies

`[GET] /api/movies/`

Response:
```
[
     {
        "id": 1,
        "name": "King Kong",
        "director": "Merian C. Cooper",
        "popularity": 80.0,
        "imdb_score": 8.0,
        "genre": [
            {
                "name": "Crime"
            },
            {
                "name": "Thriller"
            }
        ]
    },
    .
    .
    .
    {
        "id": 7,
        "name": "Metropolis",
        "director": "Fritz Lang",
        "popularity": 84.0,
        "imdb_score": 8.4,
        "genre": [
            {
                "name": "Adventure"
            },
            {
                "name": "Drama"
            },
            {
                "name": "Sci-Fi"
            }
        ]
    }
]
```

### 2. Search a Movie

`[GET] /api/movies/?search=star`

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

### 3. Fetch Movie Details

`[GET] /api/movie/5/`

Response:
```
{
    "id": 5,
    "name": "Psycho",
    "director": "Alfred Hitchcock",
    "popularity": 87.0,
    "imdb_score": 8.7,
    "genre": [
        {
            "name": "Horror"
        },
        {
            "name": "Mystery"
        },
        {
            "name": "Thriller"
        }
    ]
}
```

### 4. Create a movie

`[POST] /api/movies/`

Access is AdminOnly so need to send Authenication Header along with this request.

`'Authorization', 'Token d3e49006bc7c28d9f38932f20c5a4af5a32ccb59'`

Request:
```
{
    "id": 10,
    "name": "King Kong",
    "director": "Merian C. Cooper",
    "popularity": 80.0,
    "imdb_score": 8.0,
    "genre": [
        {"name": "Adventure"},
        {"name": "Fantasy"},
        {"name": "Horror"}
    ]
}
```

Response returns the created object:
```
{
    "id": 10,
    "name": "King Kong",
    "director": "Merian C. Cooper",
    "popularity": 80.0,
    "imdb_score": 8.0,
    "genre": [
        {"name": "Adventure"},
        {"name": "Fantasy"},
        {"name": "Horror"}
    ]
}
```

### 5. Update the movie

`[PUT] /api/movie/5/`

Access: AdminOnly (Needs Authentication)

Request:
```
{
    "id": 10,
    "name": "King Kong Part 2",
    "director": "Merian C. Cooper",
    "popularity": 85.0,
    "imdb_score": 8.5,
    "genre": [
        {"name": "Adventure"},
        {"name": "Thriller"},
        {"name": "Horror"}
    ]
}
```
Response:
```
{
    "id": 10,
    "name": "King Kong Part 2",
    "director": "Merian C. Cooper",
    "popularity": 85.0,
    "imdb_score": 8.5,
    "genre": [
        {"name": "Adventure"},
        {"name": "Thriller"},
        {"name": "Horror"}
    ]
}
```

### 6. Delete the movie

`[DELETE] /api/movie/5/`

Access: AdminOnly (Needs Authentication)

Takes no request and returns no response.


# API Testing using ajax

Visit this URL- https://fyndyashbeer.herokuapp.com/api/movies/ on chrome and press F12 to open the console.

Copy paste the following ajax snippets to test the above api endpoints.

### LIST
```
$.ajax({
    method: 'GET',
    url: '/api/movies/',
    beforeSend: function(xhr){
    },
    success: function (res) {
        console.log(res);
    },
    error: function () { // Hard failure, like network error
        console.error('Seems network error');
    }
});
```

### FETCH
```
$.ajax({
    method: 'GET',
    url: '/api/movie/1/',
    beforeSend: function(xhr){
    },
    success: function (res) {
        console.log(res);
    },
    error: function () { // Hard failure, like network error
        console.error('Seems network error');
    }
});
```

### CREATE
```
var data = {
    "popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      {"name": "Adventure"},
      {"name": "Fantasy"}
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
  }
$.ajax({
    method: 'POST',
    url: '/api/movies/',
    contentType: 'application/json',
    data: JSON.stringify(data),
    beforeSend: function(xhr){
        xhr.setRequestHeader('Authorization', 'Token d3e49006bc7c28d9f38932f20c5a4af5a32ccb59');
    },
    success: function (res) {
        console.log(res);
    },
    error: function () { // Hard failure, like network error
        console.error('Seems network error');
    }
});
```

### UPDATE
```
$.ajax({
    method: 'PUT',
    url: '/api/movie/10/',
    contentType: 'application/json',
    data: '{"name": "King Kong Part 2","director": "Merian C. Cooper","popularity": 80.0,"imdb_score": 8.0, "genre": [{"name": "Action"},{"name": "Thriller"}] }',
    beforeSend: function(xhr){
        xhr.setRequestHeader('Authorization', 'Token d3e49006bc7c28d9f38932f20c5a4af5a32ccb59');
    },
    success: function (res) {
        console.log(res);
    },
    error: function () { // Hard failure, like network error
        console.error('Seems network error');
    }
});
```

### DELETE
```
$.ajax({
    method: 'DELETE',
    url: '/api/movie/3/',
    contentType: 'application/json',
    beforeSend: function(xhr){
        xhr.setRequestHeader('Authorization', 'Token d3e49006bc7c28d9f38932f20c5a4af5a32ccb59');
    },
    success: function (res) {
        console.log(res);
    },
    error: function () { // Hard failure, like network error
        console.error('Seems network error');
    }
});
```

# Scaling up the application

First of all, deploy django app and the database on separate servers. So that we can scale the application horizontally (adding more servers when needed) and the database vertically (increasing server capacity like bigger RAM, more disk space, etc.)

**Server optimization:** We can optimize nginx and uwsgi by setting configuration parameters carefully like thread count = no. of CPU cores * 2 + 1, keepalive_timeout=30s, etc.

**Caching:** We can use Redix as primary cache for all user sessions and user lookups, because these operations are more read intensive. Also, we can cache Movie model (resource-level caching) for being read intensive.

**Configuring Load Balancer:** We can deploy application on multiple servers behind a load balancer. Since user session is managed using Redis there shouldn't be any problem with user authentication or sticky session.

**Using Elasticsearch:** We can use it for high performance movie search functionality.

**Creating Master / Slave database system:** All read operations to Slave and All write operation to the Master.

Conclusion: The bottlenecks at application are overcome by server optimization and load balancing, at database level by caching and master/slave architecture, search using elasticsearch. Using above techniques, we can scale this application to handle 75M hits per day.
