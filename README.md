# Introduction 
Luigi is the backend python service that interfaces with our Mario-React web app. 

# Getting Started
1.	Installation process
    install python 3.7.4+ or use python environment on university computers
    * Make sure python is added to your path when you install it.
    install the following python packages using pip install:
    * django
    * djangorestframework
    * django-cors-headers
    * requests
    * pyodbc
    * msrest (for manual OAuth token script)

2.	Software dependencies
    * ODBC Driver 17 for SQL server

3.	Latest releases

# Build and Test
How to run debug: 
    * navigate to `SE4330-Luigi/MarioApi/` and run the command `python manage.py runserver`.

How to run tests:
    * navigate to `SE4330-Luigi/MarioApi/` and run the command `python manage.py test ApiV1/`.
        * This command will run all tests found under ApiV1 directory. See django running unit tests documentation for narrowing
        test scope.

How to create tests:
    All tests should live under `ApiV1/UnitTests/`
    Any stubs (i.e: a sample httpresponse body from AzureDevops that is being used to test code.) that may be needed can live in UnitTests/stubs or within your test file itself if the stubs are not large (i.e: the inputs of your code that you are testing come from elsewhere in the project as simple variables).
    Each Unit test file/class should correlate to one source file and its name must start with 'test' for django's test discovery to find it. format: `test*.py`

    Test classes should inherit from `django.test.TestCase`
    See `TestConfigurationController.py` for working example of setup and tests.

How to run code coverage:
    1. Install package: `pip install coverage`
    2. Run coverage with test command: `coverage run manage.py test ApiV1/`
    3. Run report after tests finish: `coverage report` 


# Contribute
To contribute, clone this repo locally then create a feature branch and make a pull request to develop to submit your changes for review. New tests should be written for any new logic.

All Pull Requests must target develop, pass the CI build, and have 2 approvals from reviewers.