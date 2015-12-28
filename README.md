# social-environment

A web based application that allows visitors to see several of the EPA's key datasets on a map and share the results with their friends. 


Getting Started
===

This project will eventually be an open source project. Before that point, we will remove all the secrets in the repo and do a force push with a v0.1 commit history. Clone the repo to contribute

    $ git clone git@github.com:excellaco/social-environment.git
    $ cd social-environment
    $ pip install -r requirements.txt
    $ export SECRET_KEY="1"
    $ ./manage.py migrate
    $ ./manage.py runserver


Testing
===
Running tests is simple with django

    $ ./manage.py test


Addition Reading
===
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
