Build
===

Status
---
![Build Status](http://build.social-environment.com/jenkins/buildStatus/icon?job=social-environment)
Code Coverage
---
![Code Coverage](http://build.social-environment.com/jenkins/job/social-environment/cobertura/graph)


# social-environment

Social-Environment is an application that allows visitors to check their local environmental score and share it with friends.  Given a location, visitors will see a local air quality score based on EPA <a href="http://www3.epa.gov/airdata/ad_basic.html">air quality data</a> and can drill down to see individual contributing factors to the local air quality score.

For a given location, Social-Environment displays an Air Quality Score which uses EPA's Air Quality Index to rate air quality related to known pollutants that were measured in that area within the past year.


##Design Approach
**<a href="http://www.excella.com">Excella Consulting</a>** put a small team together and followed an agile development methodology to build **Social-Environment** in an iterative, incremental manner. The cross-functional team, comprised of analysts and developers, began with a brainstorming session and defined an initial Minimum Viable Product (MVP). Not being co-located, and working on the project during off-hours, the team used Slack to communicate and held conference calls every three days to ensure proper coordination.

The self-organized team not only fulfilled their individual roles in the design and development process, but also helped where needed to deliver a quality product. Utilizing **[GitHub issues](https://github.com/excellaco/social-environment/issues)**, the team created and groomed a Kanban backlog, discussed design decisions, and tracked bugs.


##Initial Concept
The team met to brainstorm initial concepts after having reviewed available EPA datasets for consumption.  We landed on Air Quality and Toxic Release Inventory data, as we thought this data might provide an opportunity for an interesting visualization.

We defined a <a href="https://github.com/excellaco/social-environment/wiki/User-Persona">user persona</a> for our prototypical user and developed it with this persona in mind.

We developed some <a href="https://github.com/excellaco/social-environment/issues/3">napkin sketches</a> to visualize our concept.  Later we worked with our graphics designer to produce some custom art for the project.

We decided to use Kanban and developed a backlog of tasks that defined the Minimum Viable Product we wanted to build for our submission.  This can be found by viewing the <a href="https://github.com/excellaco/social-environment/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Minimum+Viable+Product%22">Minimum Viable Product milestone</a> in our Github repository.  We defined additional issues and recorded enhancement requests and bugs as <a href="https://github.com/excellaco/social-environment/issues">Issues</a>.

We agreed on a meeting cadence given everyone's holiday and work schedules, and decided to use Slack for daily communication.

In the first three days we established a github repository for our code and issues.  We decided to use a Continuous Integration server to provide automated testing and deployment.  We developed an automated mechanism to download raw data files and load the pertinent data into a relational database, and a simple mechanism to display those data points on a map.  And we analyzed the data sets and data dictionaries made available by EPA to better understand the data and its usage to determine how we could use them in our visualization.

##Data
The team chose the EPA Air Quality data as the source for the Social-Environment app.  The application contains code to download the EPA data from an EPA FTP site (in Excel format) and imports the data into a Postgres database for processing by the API.  Among other fields, the dataset contains latitude, longitude, pollutant, various quantity measurements, and a year for every air quality measurement recorded.  We ran these raw data through an <a href="https://github.com/excellaco/social-environment/wiki/Air-Quality-Calculation">algorithm</a>, leveraging the EPA Air Quality Index, to generate an easy-to-understand air quality score.  This score can be applied to a person's location by taking into account the air quality scores of all pollution measurements in a 2 mile radius for the given year.


##API Methods
The design began with creating an API to access the air quality data.  The challenge was to create a function that, given a latitude and longitude, would return a series of datapoints within an arbitrary radius of that latitude and longitude.  <a href="http://www.excella.com">Excella</a> used a haversine function to do so.  Then, each datapoint is evaluated to determine an air quality score.  The API is designed to provide consumers both the relative air quality score for a region, given a location and year; and to provide the discrete pollutant occurrences for the same location and year.


### map_score
GET `/api/v1/map_score/`

The map_score service takes as optional parameters a latitude, longitude, and year and returns the air quality score of the area bounded by a 2 mile radius around the specified lat/lon.  The score is determined by choosing the highest (most hazardous) score for any compound in the radius for the specified year.

Example: `http://social-environment.com/api/v1/map_score/?latitude=38.06&longitude=-77.09&year=2013`

### airquality
GET `/api/v1/airquality`

The airquality service takes as parameters a latitude, longitude, and year and returns a collection of air quality data points within an area bounded by a 2 mile radius around the specified latitude and longitude.

Example: `http://social-environment.com/api/v1/airquality/?latitude=38.06&longitude=-77.09&year=2013`


##Tech Stack
The social-environment application has many parts. Our public facing web site is built in javascript, jquery and html and utilizes our backend services via a RESTful API to interact with the social-environment dataset. The backend is built on top of a python 2.7, django 1.8.7 and more specifically Wagtail as a CMS. Utilizing Wagtail as a CMS will allow the expansion of the site as well as easy administration of new content outside the scope of the initial release. Wagtail also includes a built-in RESTful service for potential future web applications to utilize with no development time on our part. The site also includes a basic administration console that allows our staff and super users to create new users, groups, permissions, delete, edit and create new air quality data points. The backend service stores data in a postgres database and limits its interface through the django Object Relationship Model (ORM). The use of the ORM prevents most SQL injection attacks and other vulnerabilities associated with manual SQL manipulation. The ORM handles the forward and backward migrations of the postgres database as well. We chose a version of django that would allow us the convenience of code managed migrations that are agnostic to backend database. This affords us the ability to not be locked into any single database. While testing locally, the developers often used a SQLite database. 

The resources for the example deployed version of social-environment are all managed in AWS. The build server is a Ubuntu EC2 instance running Jenkins polling our source control management at github. The production application is a AWS linux flavored EC2 instance running the web application, serving the static content, and running the postgres database service. All of these EC2 instances are on a secluded Virtual Private Cloud with a configured Internet Gateway to allow open access to the internet. A Security Group is setup to firewall access from the public except through known ports and protocols.  


Getting Started 
===
Prerequisites
---
 * git
 * python 2.7
 * pip
 * postgres

Instructions
---

    $ git clone git@github.com:excellaco/social-environment.git
    $ cd social-environment
    $ pip install -r requirements.txt
    $ export SECRET_KEY="1"
    $ ./manage.py migrate
    $ ./manage.py runserver


##Testing
To execute the tests, run the server (if it's not already running)

    $ python manage.py runserver

Then in a separate terminal window, execute the tests

	$ nosetests
    
###Code Coverage
To generate a code coverage report, use the jenkins command. It will also run your tests. 

    $ ./manage.py jenkins --enable-coverage
    $ ls reports



##Deployment
<a href="http://www.excella.com">Excella</a> used Jenkins as a Continuous Integration Server and established a delivery pipeline to build, test, and deploy to an Amazon Web Services (AWS) stack upon checkin to the Git repository.  The Jenkins <a href="http://build.social-environment.com/jenkins/job/social-environment"/>build history</a> is available to the public.  Jenkins is configured to use Cobertura, a static code analysis tool, to report unit test coverage and other analysis.  Test results are available <a href="http://build.social-environment.com/jenkins/job/social-environment/75/cobertura/ ">here</a>.
