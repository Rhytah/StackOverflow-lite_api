[![Build Status](https://travis-ci.org/Rhytah/stackoverflow-lite_api.svg?branch=tests)](https://travis-ci.org/Rhytah/stackoverflow-lite_api)

[![Coverage Status](https://coveralls.io/repos/github/Rhytah/stackoverflow-lite_api/badge.svg?branch=tests)](https://coveralls.io/github/Rhytah/stackoverflow-lite_api?branch=tests)

[![Maintainability](https://api.codeclimate.com/v1/badges/bd3703ac4e0a2f68396a/maintainability)](https://codeclimate.com/github/Rhytah/stackoverflow-lite_api/maintainability)


# stackoverflow-lite_api

StackOverflow-lite_Api is an interface that comprises of a set of endpoints that use data structures to store data in memory

### Tools

* Text editor where we write our project files. (VScode)
* Python
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library 
* Postman -Application to test and consume endpoints
* PEP8 - Style guide

## Getting Started
clone the github repo to your computer:
* $git clone https://github.com/Rhytah/stackoverflow-lite_api
* Extract the zip file to another file

**Create virtual environment and activate it**
```
$pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
``` 
 **Install all the necessary tools by**
 ```
 $pip insatll -r requirements.txt
 ```
**Start app server in console/terminal/commandprompt**
```
$python app.py
```
**Run tests on requests**
```
pytest tests/test_requests.py
```
**Run tests while listing every run test**
```
pytest tests/test_requests.py -v
```
## Versioning
```
This is version one"v1" of the API
```
**API app is hosted at**
```
https://rhytahapi.herokuapp.com/
```
## End Points
|           End Point                            |            Functionality                   |
|   ------------------------------------------   | -----------------------------------------  |
|     GET  api/v1/questions                      |             Fetch all questions            |
|     GET  api/v1/questions/<question_id>        |             Fetch a question               |
|     POST api/v1/questions                      |             Add a question                 |
|     POST api/v1/question/<question_id>/answers |             Add an answer                  |

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/c6713f96622f32b859ba)

## Author
- [Rhytah] https://github.com/Rhytah



