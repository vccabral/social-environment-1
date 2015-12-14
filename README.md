# social-environment

A web based application that allows visitors to see several of the EPA's key datasets on a map and share the results with their friends. 


Getting Started
===

This project will eventually be an open source project. Before that point, we will remove all the secrets in the repo and do a force push with a v0.1 commit history. Clone the repo to contribute

    $ git clone git@github.com:excellaco/social-environment.git
    $ cd social-environment
    $ ./manage.py migrate
    $ ./manage.py import_raw_data
    $ ./manage.py tranform_raw_data # write me
    $ ./manage.py runserver

Testing
===
Running tests is simple with django

    $ ./manage.py test


