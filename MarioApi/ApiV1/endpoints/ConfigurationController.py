# -*- coding: utf-8 -*-
from .GitCaller import GitCaller
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from django.http import HttpResponse
import json
"""
Created on Mon Dec  2 17:27:05 2019

@author: cruzga
"""
    
def get_DevData(request):
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response
    token = request.headers['azure']
    organization = request.headers['organization']
    util = Utilities(token, organization)
    git_caller = GitCaller(util)
    database  = DatabaseCaller()
    project = request.GET["project"]
    repo = request.GET["repo"]
    branchdata = json.loads(git_caller.get_listOfBranches(project,repo))['value']

    branches = []
    for branch in branchdata:
        branchName = branch['name'].split('/')[2]
        branches.append(branchName)
        
    drive_types = database.drive_types_get()
    environments = database.environment_get()
    
    data = {"TestEnv" : environments, "DriveType" : drive_types, "Branches" : branches}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response
        
            
