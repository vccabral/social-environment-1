# social-environment

Social Environment is an application that allows visitors to check their local environmental score and share it with friends.  Given a location, visitors will see a local air quality score based on FDA air quality data and can drill down to see individiual contributing factors to the local air quality score.


Getting Started
===

This project will eventually be an open source project. Before that point, we will remove all the secrets in the repo and do a force push with a v0.1 commit history. Clone the repo to contribute

    $ git clone git@github.com:excellaco/social-environment.git
    $ cd social-environment
    $ pip install -r requirements.txt
    $ export SECRET_KEY="1"
    $ ./manage.py migrate
    $ ./manage.py runserver


Design
===
Describe our tech solution approach.  E.g. django api tools, mapping tools, data source, etc.


API
===
Describe the use and function of the API, including how to access it.


Testing
===
Running tests is simple with django

    $ ./manage.py test


Deployment
===
Let's provide instructions for how to deploy to Heroku or AWS, if that's the route we take.  Let's also talk about CI here.


Additional Reading
===

Do we need this section?

elasticsearch gis route
---
http://blog.trifork.com/2013/08/01/server-side-clustering-of-geo-points-on-a-map-using-elasticsearch/
https://www.elastic.co/blog/geo-location-and-search

heroku postgres gis route
---
https://devcenter.heroku.com/articles/heroku-postgres-extensions-postgis-full-text-search#postgis
https://devcenter.heroku.com/articles/postgis
https://github.com/cyberdelia/heroku-geo-buildpack/

front end gis route
---
https://github.com/turfjs/turf
