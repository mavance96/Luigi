import json
import requests
import http
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from .BuildsCaller import BuildsCaller
from .TestRunsCaller import TestRunCaller
from .BuildDefinitionCaller import BuildDefinitionCaller
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

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
    pcArtifacts = jsonbody["PCArtifacts"]
    appArtifacts = jsonbody["APPArtifacts"]
    ccArtifacts = jsonbody["CCArtifacts"]
    numberOfRuns = jsonbody["numberOfRuns"]
    
    dbCaller = DatabaseCaller()
    buildId = dbCaller.buildIDs_get(driveType, testEnv)
    build_responses = []
    for num in range(0, numberOfRuns):
        build = buildcaller.queue_build(project, buildId, pcArtifacts, appArtifacts, ccArtifacts)
        build_responses.append(build)
    failedResponses = 0
    responseNotFound = False
    for build in build_responses:
        if build != 200:
            failedResponses += 1
        if build == 404:
            responseNotFound = True
    body = json.dumps({"failedResponses": failedResponses, "numberOfRuns": numberOfRuns, "build": 6})
    response = HttpResponse(status= http.HTTPStatus.OK)
    if responseNotFound == True:
        response = HttpResponse(status=http.HTTPStatus.NOT_FOUND)
    if failedResponses > 0:
        response = HttpResponse(status= http.HTTPStatus.BAD_REQUEST)
    response["Access-Control-Allow-Origin"] = "*"
    response.content = body
    return response


def list_of_builds(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    token = request.headers["azure"]
    organization = request.headers["organization"]
    project = request.GET["project"]
    util = Utilities(token, organization)
    buildCaller = BuildsCaller(util)
    today = datetime.now()
    lastWeek = today - timedelta(days=7)
    
    buildParams = {"minTime" : str(lastWeek.isoformat())}

    rawBuildData = buildCaller.get_listOfBuilds(project, buildParams)
    if type(rawBuildData) == int:
        return HttpResponse(status=rawBuildData)
    buildData = json.loads(rawBuildData)['value']

    buildsList = []
    for build in buildData:
        if build['status'] == 'completed':
            result = build['result']
            finishTime = build['finishTime']
            finishTime = finishTime[0:19]
            finishTime = datetime.strptime(finishTime, "%Y-%m-%dT%H:%M:%S").strftime('%m/%d/%Y %I:%M%p')
        else:
            result = 'inProgress'
            finishTime = 'inProgress'
            
        queuedTime = build['queueTime']
        queuedTime = queuedTime[0:19]
        queuedTime = datetime.strptime(queuedTime, "%Y-%m-%dT%H:%M:%S").strftime('%m/%d/%Y %I:%M%p')
        author = build['requestedBy']
        authors = author['displayName']
        ratio = list_of_test_runs(util, build['id'], project)
        buildsList.append({"id": build['id'], "buildNumber": build['buildNumber'], "finishedTime": finishTime,
                           "status": build['status'], "author": authors, 'tags': build['tags'], 'results': result,
                           'queuedTime': queuedTime, 'ratio' : ratio})
    data = {'builds': buildsList}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def getLastBuild(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    token = request.headers["azure"]
    organization = request.headers["organization"]
    project = request.GET['project']
    nameId = request.GET['nameId']
    util = Utilities(token, organization)
    buildcaller = BuildsCaller(util)
    lastBuild = buildcaller.get_latestBuild(project, 1, nameId)
    response = HttpResponse(lastBuild, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response
    
#This function gets tye list of runs and find the ratio for the lastest run on build by Gabe
def list_of_test_runs(util, buildId, project):
    testRunsCaller = TestRunCaller(util)
    testRunData = json.loads(testRunsCaller.get_list_of_runs(project, buildId))['value']
    if testRunData == []:
        return 'No Tests'
    totalTests = []
    passedTests = []
    for test in testRunData:
        totalTests.append(test['totalTests'])
        passedTests.append(test['passedTests'])
    # incompleteTests = testRun['incompleteTests']
    # completedTests = totalTests - incompleteTests
    ratio = str(passedTests.pop()) +'/' + str(totalTests.pop())
    return ratio
