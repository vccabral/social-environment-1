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


Design Approach
===
Given the short turnaround-time and proximity to planned holiday vacation, **Excella Consulting** put a small team together to and followed an agile development framework to build **Social-Environment** in an iterative, incremental manner. The cross-functional team, comprised of analysts, designers, and developers, began with Sprint 0, followed by three-day sprints. Not being co-located, and working on the project during off-hourse, the team used Slack to communicate and held conference calls every three days to ensure proper coordination.

The team consisted of the following roles:

* Product Manager
* Technical Architect
* User Researcher/Usability Tester
* Visual Designer
* Front-End Web Developers
* Back-End Web Developers
* DevOps Engineer
* Business Analyst

The self-organized team not only fulfilled their individual roles in the design and development process, but also helped where needed to deliver a quality product. The Product Manager led the effort with a focus on the value delivered by the final product, enabling the team to respond quickly to changing priorities and address feedback from usability testing. Utilizing **[GitHub issues](https://github.com/excellaco/social-environment/issues)**, the team created and groomed a backlog, discussed design decisions, and tracked bugs.


API
===
Describe the use and function of the API, including how to access it.
The design began with creating an API to access the data.  The challenge was to create a function that, given a latitude and longitude, would return a series of datapoints within an arbitrary radius of that latitude and longitude.  Excella used a haversine function to do so.  Then, each datapoint is evaluated 


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
