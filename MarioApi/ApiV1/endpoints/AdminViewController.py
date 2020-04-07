# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:37:13 2020
Admin View Endpoint handling file. Contains functions related to fulfilling API requests
for data this needed by the front-end admin view.
authors: cruzga, postmaj, priort
"""
import json

import http

from django.views.decorators.csrf import csrf_exempt

from .DatabaseCaller import DatabaseCaller
from django.http import HttpResponse


@csrf_exempt
def endpoint_driveTypes(request):
    """Drive Types endpoint handling method. Checks the request type and passes it to the correct method"""
    """Endpoint: <>/api/driveTypes"""
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, DELETE, PATCH"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    dbCaller = DatabaseCaller()
    if request.method == "GET":
        response = get_driveTypes(dbCaller)
    else:
        jsonbody = json.loads(request.body)
        if request.method == "POST":
            driveType = jsonbody["name"]
            response = post_driveTypes(dbCaller, driveType)
        elif request.method == "PATCH":
            oldDriveType = jsonbody["oldName"]
            newDriveType = jsonbody["newName"]
            response = patch_driveTypes(dbCaller, oldDriveType, newDriveType)
        elif request.method == "DELETE":
            driveType = jsonbody["name"]
            response = delete_driveTypes(dbCaller, driveType)
        else:
            response = HttpResponse(status=400)
    response["Access-Control-Allow-Origin"] = "*"
    return response


@csrf_exempt
def endpoint_environments(request):
    """Environments Handling Endpoint handling method. Checks the request type and passes it to the correct method"""
    """Endpoint: <>/api/environments"""
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, DELETE, PATCH"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    dbCaller = DatabaseCaller()
    if request.method == "GET":
        response = get_environments(dbCaller)
    else:
        jsonbody = json.loads(request.body)
        if request.method == "POST":
            environment = jsonbody["name"]
            response = post_environments(dbCaller, environment)
        elif request.method == "PATCH":
            oldEnvironment = jsonbody["oldName"]
            newEnvironment = jsonbody["newName"]
            response = patch_environments(dbCaller, oldEnvironment, newEnvironment)
        elif request.method == "DELETE":
            environment = jsonbody["name"]
            response = delete_environments(dbCaller, environment)
    response["Access-Control-Allow-Origin"] = "*"
    return response


@csrf_exempt
def endpoint_buildmaps(request):
    """Build Map Handling method. Checks the request type and passes it to the correct method"""
    """Endpoint: <>/api/buildmaps"""
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, DELETE, PATCH"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    dbCaller = DatabaseCaller()
    if request.method == "GET":
        response = get_buildmaps(dbCaller)
    else:
        jsonbody = json.loads(request.body)
        if request.method == "POST":
            buildId = jsonbody["buildid"]
            driveType = jsonbody["drivetype"]
            environment = jsonbody["environment"]
            response = post_buildmaps(dbCaller, buildId, driveType, environment)
        elif request.method == "PATCH":
            oldBuildId = jsonbody["oldbuildid"]
            buildId = jsonbody["buildid"]
            driveType = jsonbody["drivetype"]
            environment = jsonbody["environment"]
            response = patch_buildmaps(dbCaller, oldBuildId, buildId, driveType, environment)
        elif request.method == "DELETE":
            buildId = jsonbody["buildid"]
            response = delete_buildmaps(dbCaller, buildId)
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_driveTypes(dbCaller):
    """Get Drive Types request handling method. Returns a list of all Drive types stored in the database"""
    driveTypes = dbCaller.drive_types_get()
    driveList = []
    for driveRow in driveTypes:
        driveName = driveRow
        driveList.append({'name': driveName})
    data = {'drivetypes': driveList}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response


def post_driveTypes(dbCaller, driveType):
    """"Post Drive types Request handling method. Inserts a new drive type in the database with the provided name"""
    if dbCaller.drive_types_insert(driveType):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def patch_driveTypes(dbCaller, oldDriveType, newDriveType):
    """Patch Drive types Request handling method. Changes the name of a drive type from the database with the"""
    """provided original name to the new provided name"""
    if dbCaller.drive_types_update(oldDriveType, newDriveType):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def delete_driveTypes(dbCaller, driveType):
    """"Delete Drive types Request handling method. Deletes a drive type from the database with the provided name"""
    if dbCaller.drive_types_delete(driveType):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def get_environments(dbCaller):
    """Get Environments request handling method. Returns a list of the environments from the database"""
    environmentList = []
    environment = dbCaller.environment_get()
    for environmentRow in environment:
        environmentName = environmentRow
        environmentList.append({'name': environmentName})
    data = {'environments': environmentList}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response


def post_environments(dbCaller, environment):
    """Post Environments request handling method. Adds a new environment to the database with the provided name"""
    if dbCaller.environment_insert(environment):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def patch_environments(dbCaller, oldEnvironment, newEnvironment):
    """Patch Environments request handling method. Changes the environment in the database with the provided name"""
    """to the new environment name provided"""
    if dbCaller.environment_update(oldEnvironment, newEnvironment):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def delete_environments(dbCaller, environment):
    """Delete Environments request handling method. Removes the environment with the provided name from the database"""
    if dbCaller.environment_delete(environment):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def get_buildmaps(dbCaller):
    """Get Build Maps request handling method. Returns a list of the build mappings stored in the database"""
    mappings = dbCaller.buildIDs_getMaps()
    mappingList = []
    for mappingRow in mappings:
        buildId = mappingRow[0]
        driveType = mappingRow[1]
        environment = mappingRow[2]
        mappingList.append({"buildid": buildId, "environment": environment, "drivetype": driveType})
    data = {'buildmaps': mappingList}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response


def post_buildmaps(dbCaller, buildId, driveType, environment):
    """Post Build Maps request handling method. Adds a new build mapping to the database with the provided"""
    """parameters"""
    if dbCaller.buildIDs_insert(buildId, driveType, environment):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def patch_buildmaps(dbCaller, oldBuildId, buildId, driveType, environment):
    """Patch Build Maps request handling method. Updates a build mapping with the provided old build id, with the"""
    """new provided params"""
    if dbCaller.buildIDs_patch(oldBuildId, buildId, driveType, environment):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def delete_buildmaps(dbCaller, buildId):
    """Delete Build Mapping request handling method. Removes the build mapping with the provided build id from the """
    """database"""
    if dbCaller.buildIDs_delete(buildId):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
