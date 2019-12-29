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
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "azure, organization"
        return response
    
    token = request.headers['azure']
    organization = request.headers['organization']
    project = request.GET["project"]
    repo = request.GET["repo"]

    util = Utilities(token, organization)
    git_caller = GitCaller(util)
    database  = DatabaseCaller()
    branchdata = git_caller.get_listOfBranches(project,repo)

    branches = __parseBranchData(branchData)
        
    drive_types = database.drive_types_get()
    environments = database.environment_get()
    
    data = {"TestEnv" : environments, "DriveType" : drive_types, "Branches" : branches}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response
        
            
def parseBranchData(branchData):
    branchjson = json.loads(branchData)['value']
    branches = []
    for branch in branchjson:
        branchName = branch['name'].split('/')[2]
        branches.append(branchName)
    return branches