# Introduction 
Luigi is the backend python service that interfaces with our react web app. 

# Getting Started
1.	Installation process
    install python 3.7.4+ or use python environment on university computers
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
4.	API references
    * Queue a build:
        [POST] `/api/queue`
        Expected request body:
        ```
        {
            
        }
        ```
    * Get dev view data:
        [GET] `/api/config`
        Expected request body:
        ```
        {

        }
        ```

        Response body:
        ```
        {
            "testenv": [],
            "drivetypes": [],
            "branches": []
        }
        ``

# Build and Test
How to run debug: 
    * navigate to `SE4330-Luigi/MarioApi/` and run the command `python manage.py runserver`.

How to run tests:
    * navigate to `SE4330-Luigi/MarioApi/` and run the command `test command`.

# Contribute
To contribute, clone this repo locally then create a feature branch and make a pull request to develop to submit your changes for review. New tests should be written for any new logic.