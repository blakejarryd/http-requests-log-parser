# HTTP requests log analysis

## What is for?

An application that parses a http request log file and returns statistics.

## Assumptions
1. The log file is aways in the following format
`177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /intranet-analytics/ HTTP/1.1" 200 3574`

2. When calculating top stats - all requests are considered valid. Irrespetive of HTTP method or response code.
e.g. A response code of 404 (not found error) will still be included in the top url calculations. 

3. Only one file needs to be parsed at a time

## Dependancies
- python3
(https://www.python.org/downloads/) 
- pytest (to run tests only)
(https://docs.pytest.org/en/7.1.x/getting-started.html)

## Instructions
- Clone this respository
- Move the http log file to be analyzed into the root directory
- Run the 'app.py' file with python3
~~~
$ python3 app.py
~~~
- Enter the log file name (including extension in the terminal)


## Tests
- Tests have been written using pytest to validate the log statistics using the 'test-data.log' file
- To run the tests run the 'tests.py file with pytest
~~~
$ pytest tests.py
~~~

