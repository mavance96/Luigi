import json
import requests
import http
from .Utilities import Utilities
from .DatabaseCaller import DatabaseCaller
from .BuildDefinitionCaller import BuildDefinitionCaller
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_listOfPipelines(request):
    """
    Retrieves list of pipelines in the requested project
    Endpoint: <>/api/pipelines
    :param request: HTTP Request passed on from Django
    :return: HTTP Response containing requested Data
    """
    if request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Allow-Headers"] = "azure, organization, Content-Type"
        return response
    token = request.headers["azure"]
    organization = request.headers["organization"]

    # Mandatory params
    project = request.GET.get("project")

    # Optional params
    dateFrom = request.GET.get("dateFrom")
    metricParams = {}
    if(dateFrom):
        metricParams['dateFrom'] = dateFrom

    util = Utilities(token, organization)
    pipelineParams = {"includeLatestBuilds": "true"}
    bdCaller = BuildDefinitionCaller(util)

    pipelineData = bdCaller.get_buildDefinitions(project, pipelineParams)

    if type(pipelineData) == int:
        return HttpResponse(status=pipelineData)

    pipelineData = json.loads(pipelineData)['value']

    pipelineList = []
    for rawPipeline in pipelineData:
        pipeline = {}
        pipeline['id'] = rawPipeline['id']
        pipeline['name'] = rawPipeline['name']
        latestBuild = rawPipeline.get('latestBuild', "")
        if latestBuild:
            pipeline['recentBuildId'] = latestBuild['id']
        metricData = bdCaller.get_buildDefinitionMetrics(project, pipeline['id'], metricParams)
        cancelledBuilds = 0;
        failedBuilds = 0;
        partiallySuccessfulBuilds = 0;
        successfulBuilds = 0;
        totalBuilds = 0

        if type(metricData) != int:
            for datum in json.loads(metricData)['value']:
                dataType = datum['name']
                value = datum['intValue']
                if dataType == "FailedBuilds":
                    failedBuilds += value
                elif dataType == "PartiallySuccessfulBuilds":
                    partiallySuccessfulBuilds += value
                elif dataType == "SuccessfulBuilds":
                    successfulBuilds += 1
                elif dataType == "TotalBuilds":
                    totalBuilds += 1
                elif dataType == "CanceledBuilds":
                    cancelledBuilds += 1
        pipeline["failedBuilds"] = failedBuilds
        pipeline["cancelledBuilds"] = cancelledBuilds
        pipeline["partiallySuccessfulBuilds"] = partiallySuccessfulBuilds
        pipeline["successfulBuilds"] = successfulBuilds
        pipeline["totalBuilds"] = totalBuilds

        pipelineList.append(pipeline)

    data = {"pipelines" : pipelineList}
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response
