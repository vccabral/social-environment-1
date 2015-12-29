Build
===

Status
---
![Build Status](http://build.social-environment.com/jenkins/buildStatus/icon?job=social-environment)
Code Coverage
---
![Code Coverage](http://build.social-environment.com/jenkins/job/social-environment/cobertura/graph)


# social-environment

Social Environment is an application that allows visitors to check their local environmental score and share it with friends.  Given a location, visitors will see a local air quality score based on EPA <a href="http://www3.epa.gov/airdata/ad_basic.html">air quality data</a> and can drill down to see individiual contributing factors to the local air quality score.

For a given location, Social-Environment displays an Air Quality Score which uses EPA's Air Quality Index to rate air quality related to known pollutants that were measured in that area within the past year.


##Design Approach
**Excella Consulting** put a small team together and followed an agile development framework to build **Social-Environment** in an iterative, incremental manner. The cross-functional team, comprised of analysts and developers, began with Sprint 0, followed by three-day sprints. Not being co-located, and working on the project during off-hours, the team used Slack to communicate and held conference calls every three days to ensure proper coordination.

The self-organized team not only fulfilled their individual roles in the design and development process, but also helped where needed to deliver a quality product. Utilizing **[GitHub issues](https://github.com/excellaco/social-environment/issues)**, the team created and groomed a Kanban backlog, discussed design decisions, and tracked bugs.


##Sprint 0
*Include detail here from our first brainstorming session, application concent, user persona, and roadmap.*


##Data
The team chose the EPA Air Quality data as the source for the Social-Environment app.  The application contains code to download the EPA data from an EPA FTP site (in Excel format) and imports the data into a Postgres database for processing by the API.  Deploying the code that downloads the data can take a bit of time - up to an hour.  *Need detail here.  We need to include our interpretation of the data and the AQI scoring.*

##API Methods
The design began with creating an API to access the air quality data.  The challenge was to create a function that, given a latitude and longitude, would return a series of datapoints within an arbitrary radius of that latitude and longitude.  Excella used a haversine function to do so.  Then, each datapoint is evaluated to determine an air quality score.  The API is designed to provide consumers both the relative air quality score for a region, given a location and year; and to provide the discrete pollutant occurrances for the same location and year.


### map_score
GET `/api/v1/map_score/`

The map_score service takes as optional parameters a latitude, longitude, and year and returns the air quality score of the area bounded by a X mile radius around the specified lat/lon.  The score is determined by choosing the highest (most hazardous) score for any compound in the radius for the specified year.

Example: `http://social-environment.com/api/v1/map_score/?latitude=38.06&longitude=-77.09&year=2013`

### airquality
GET `/api/v1/airquality`

The airquality service takes as parameters a latitude, longitude, and year and returns a collection of air quality data points within an area bounded by a X mile radius around the specified latitude and longitude.

Example: `http://social-environment.com/api/v1/airquality/?latitude=38.06&longitude=-77.09&year=2013`


##Tech Stack
The social-environment application has many parts. Our public facing web site is built in javascript, jquery and html and utilizes our backend services via a RESTful API to interact with the social environment dataset. The backend is built on top of a python 2.7, django 1.8.7 and more specifically Wagtail as a CMS. Utilizing Wagtail as a CMS will allow the expansion of the site as well as easy adminstration of new content outside the scope of the initial release. Wagtail also includes a built in RESTful service for potential future web applications to utilize with no development time on our part. The site also includes an basic adminstration console that allows our staff and super users to create new users, groups, permissions, delete, edit and create new air quality data points. The backend service stores data in a postgres database and limits its interface through the django Object Relatioship Model (ORM). The use of the ORM prevents most SQL injection attacks and other vulnerabilities associated with manual SQL manipulation. The ORM handles the forward and backward mgrations of the postgres database as well. We chose a version of django that would allow us the convience of code managed migrations that are agnostic to backend database. This affords us the ability to not be locked into any single database. While testing locally, the developers often used a SQLite database. 

The resources for the example deployed version of social-environment are all managed in AWS. The build server is a Ubuntu EC2 instance running Jenkins polling our source control management at github. The production application is a AWS linux flavored EC2 instance running the web application, serving the static content, and running the postgres database service. All of these EC2 instances are on a secluded Virtual Private Cloud with a configured Internet Gateway to allow open access to the internet. A Security Group is setup to firewall access from the public except through known ports and protocols.  


##Installing from Source
This project will eventually be an open source project. Before that point, we will remove all the secrets in the repo and do a force push with a v0.1 commit history. Clone the repo to contribute

    $ git clone git@github.com:excellaco/social-environment.git
    $ cd social-environment
    $ pip install -r requirements.txt
    $ export SECRET_KEY="1"
    $ ./manage.py migrate
    $ ./manage.py runserver


##Testing
Running tests is simple with django

    $ ./manage.py test
    
###Code Coverage
To generate a code coverage report, use the jenkins command. It will also run your tests. 

    $ ./manage.py jenkins --enable-coverage
    $ ls reports



##Deployment
Excella used Jenkins as a Continuous Integration Server and established a delivery pipeline to build, test, and deploy to an Amazon Web Services (AWS) stack upon checkin to the Git repository.  *Need more detail here.  Ideally they can somehow recreate this deployment enviroment.*


##Additional Reading
*Do we need this section?*

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
