# -*- coding: utf-8 -*-
from .GitCaller import GitCaller
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from django.http import HttpResponse
from .ProjectCaller import ProjectCaller
from http import HTTPStatus
import json
import http
"""
Created on Mon Dec  2 17:27:05 2019

@author: cruzga
"""
    
def get_DevData(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response
    
    token = request.headers['azure']
    organization = request.headers['organization']
    project = request.GET["project"]
    repo = request.GET["repo"]

    util = Utilities(token, organization)
    git_caller = GitCaller(util)
    database = DatabaseCaller()
    branchdata = git_caller.get_listOfBranches(project, repo)

    branches = parseBranchData(branchdata)
        
    drive_types = database.drive_types_get()
    environments = database.environments_get()

    data = {"TestEnv": environments, "DriveType": drive_types, "Branches": branches}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def getProjectsInOrganization(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response
    
    token = request.headers['azure']
    organization = request.headers['organization']
    
    util = Utilities(token, organization)
    
    projectCaller = ProjectCaller(util)

    rawProjects = projectCaller.get_listOfProjects()
    if type(rawProjects) == int:
        response = HttpResponse(status=rawProjects)
    else:
        projectsJson = json.loads(rawProjects)

        projectNames = []

        for projects in projectsJson['value']:
            projectNames.append(projects['name'])

        data = {"Projects": projectNames}
        response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


def parseBranchData(branchData):
    branchjson = json.loads(branchData)['value']
    branches = []
    # for branch in branchjson:
    #     branchName = branch['name'].split('/')[2]
    #     branches.append(branchName)
    # return branches


def createConfiguration(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response
    elif request.method == "POST":
        db = DatabaseCaller()
        jsonbody = json.loads(request.body)
        configID = jsonbody["configid"]
        buildID = jsonbody["buildid"]
        applicationID = jsonbody["applicationid"]
        firmwareID = jsonbody["firmwareid"]
        powercardID = jsonbody["powercardid"]
        success = db.configurations_insert(configID, buildID, applicationID, firmwareID, powercardID)
        if success:
            response = HttpResponse(status=HTTPStatus.OK)
            response["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            response = HttpResponse(status=HTTPStatus.BAD_REQUEST)
            response["Access-Control-Allow-Origin"] = "*"
            return response
    else:
        response = HttpResponse(status=HTTPStatus.BAD_REQUEST)
        response["Access-Control-Allow-Origin"] = "*"
        return response


def deleteConfiguration(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = ""
        return response
    elif request.method == "DELETE":
        db = DatabaseCaller()
        jsonbody = json.loads(request.body)
        configID = jsonbody["configid"]
        success = db.configurations_delete(configID)
        if success:
            response = HttpResponse(status=HTTPStatus.OK)
            response["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            response = HttpResponse(status=HTTPStatus.BAD_REQUEST)
            response["Access-Control-Allow-Origin"] = "*"
            return response
    else:
        response = HttpResponse(status=HTTPStatus.BAD_REQUEST)
        response["Access-Control-Allow-Origin"] = "*"
        return response


def updateConfiguration(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "PUT, OPTIONS"
        response["Access-Control-Allow-Headers"] = ""
        return response
    elif request.method == "PUT":
        db = DatabaseCaller()
        jsonbody = json.loads(request.body)
        configID = jsonbody["configid"]
        buildID = jsonbody["buildid"]
        applicationID = jsonbody["applicationid"]
        firmwareID = jsonbody["firmwareid"]
        powercardID = jsonbody["powercardid"]
        success = db.configurations_update(configID, buildID, applicationID, firmwareID, powercardID)
        if success:
            response = HttpResponse(status=HTTPStatus.OK)
            response["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            response = HttpResponse(status=HTTPStatus.BAD_REQUEST)
            response["Access-Control-Allow-Origin"] = "*"
            return response
    else:
        response = HttpResponse(status=HTTPStatus.BAD_REQUEST)
        response["Access-Control-Allow-Origin"] = "*"
        return response


def printConfiguration(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = ""
        return response
    elif request.method == "GET":
        db = DatabaseCaller()
        jsonbody = json.loads(request.body)
        configInfo = db.configurations_get(jsonbody['configName'])
        response = HttpResponse(json.dumps(configInfo), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        response = HttpResponse(status=HTTPStatus.BAD_REQUEST)
        response["Access-Control-Allow-Origin"] = "*"
        return response
