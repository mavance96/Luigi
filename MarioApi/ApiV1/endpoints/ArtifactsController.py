from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from .ArtifactsCaller import ArtifactsCaller
from django.http import HttpResponse 
from django.http import HttpRequest
from http import HTTPStatus
import json


#How to publish an artifact
def get_ArtifactData(request : HttpRequest):
    """
    This gets all of the artifacts for a 
    specific drive type and test environment.
    Parameters:
        request (HttpRequest) : The request from the front end
    Returns:
        HttpResponse: The list of artifacts or if none where found 
        an empty array of values with count zero is returned.
    """

    emptyResponse = { "count" : 0, "value" : []}
    defaultResponse = HttpResponse(status=HTTPStatus.BAD_REQUEST)
    #Get the headers
    #Setup the utilities class and artifacts class objects
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    if (request.method == "GET"):

        ##Required parameters
        project = request.GET['project']
        driveType = request.GET['driveType']
        testEnv = request.GET['testEnv']
        token = request.headers['azure']
        organization = request.headers['organization']
        util = Utilities(token, organization)
        ac = ArtifactsCaller(util)

        ##Find the buildId for the parameters specified
        dbCaller = DatabaseCaller()
        buildId = dbCaller.buildIDs_get(driveType, testEnv)
        buildId = 685#For testing purposes
        if buildId == None:
            return HttpResponse(status=HTTPStatus.OK, reason="Could not find a build with specified parameters")
        ##Select the correct function
        try:
            artifact_name = request.GET['name']
            data = ac.get_ArtifactByName(project, buildId, artifact_name)
            if(data == HTTPStatus.NOT_FOUND):
                response = HttpResponse(json.dumps(emptyResponse), content_type="application/json", status=HTTPStatus.OK)
                response["Access-Control-Allow-Origin"] = "*"
                return response
            else:
                response = HttpResponse(data, content_type="application/json")
                response["Access-Control-Allow-Origin"] = "*"
                return response
        except:##If no name, give a list of artifacts
            data = ac.get_ListOfArtifacts(project, buildId)
            if(data == HTTPStatus.NOT_FOUND):
                response = HttpResponse(json.dumps([]), content_type="application/json", status=HTTPStatus.OK)
                response["Access-Control-Allow-Origin"] = "*"
                return response
            response = HttpResponse(data, content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            return response
    else:
        return defaultResponse
