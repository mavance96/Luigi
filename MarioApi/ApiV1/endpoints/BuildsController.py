import json
import requests
import http
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from .BuildsCaller import BuildsCaller
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def queue_build(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    token = request.headers["azure"]
    organization = request.headers["organization"]
    jsonstring = request.body
    jsonbody = json.loads(jsonstring)
    util = Utilities(token, organization)
    buildcaller = BuildsCaller(util)

    project = jsonbody["project"]
    testEnv = jsonbody["testEnv"]
    driveType = jsonbody["driveType"]
    
    dbCaller = DatabaseCaller()
    buildId = dbCaller.buildIDs_get(driveType, testEnv)
    build = buildcaller.queue_build(project, buildId)

    if build == 200:
        response = HttpResponse(status= http.HTTPStatus.OK)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    if build == 404:
        response = HttpResponse(status=http.HTTPStatus.NOT_FOUND)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        response = HttpResponse(status= http.HTTPStatus.SERVICE_UNAVAILABLE)
        response["Access-Control-Allow-Origin"] = "*"
        return response