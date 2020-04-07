from .Utilities import Utilities
import json
from django.http import HttpResponse
from django.http import HttpRequest
from http import HTTPStatus


class BuildsCaller:
    def __init__(self, util):
        self.util = util

    def get_buildByID(self, project, build_id):
        """
        Returns a build and its information, given an id
        :param build_id:  Your "absolute" build id
        :return: Build information
        """
        requestURL = "/" + project + "/_apis/build/builds/" + str(build_id)
        return self.util.getRequest(requestURL)

    def get_listOfBuilds(self, project, params={}):
        """
        Returns a list of all builds in the project
        :return:  All build information
        """
        requestURL = "/" + project + "/_apis/build/builds"
        return self.util.getRequest(requestURL, params)

    def queue_build(self, project, build_id, pcArtifacts, appArtifacts, ccArtifacts):
        """
        Queues a build, given the ID and list of additional parameters
        :param build_id: Your "unique" build ID.
       
        :return: status code (hopefully 2xx)
        """
        parameterStr = "\"APPArtifactName\" : \"{}\",\"PCArtifactName\" : \"{}\",\"CCArtifactName\" : \"{}\","\
            .format(appArtifacts, pcArtifacts,ccArtifacts)
        data = {
            "parameters" : "{" + parameterStr + "}",
            "definition" : {"id": build_id}
        }

        requestURL = "/" + project + "/_apis/build/builds"
        return self.util.postRequest(requestURL, json.dumps(data))

    def delete_build(self, project, build_id):
        """
        Deletes a specified build, given an ID.
        :param build_id: Your "absolute" build ID
        :return: status code (hopefully 2xx)
        """
        requestURL = "/" + project + "/_apis/build/builds/" + str(build_id)
        return self.util.deleteRequest(requestURL)

    def get_buildLogs(self, project, build_id):
        """
        Gets build logs for a specific build
        :return: All build logs information
        """
        requestURL = "/" + project + "/_apis/build/builds/" + str(build_id) + "/logs"
        return self.util.getRequest(requestURL)

    def get_buildLog(self, project, build_id, log_id):
        """
        Gets specific build log, given build_id and log_id
        :param build_id: Your "absolute" build id
        :param log_id: Your log id for that build
        :return: Build log information
        """
        requestURL = "/" + project + "/_apis/build/builds/" + str(build_id) + "/logs/" + str(log_id)
        return self.util.getRequest(requestURL)
                                                                
    def get_latestBuild(self, project, numBuilds, requestedFor):
        """
        Gets the last build of a user and its information, 
        given an a start time and user's name
        :param top: The maximum number of builds to return
        :param requestedFor: If specified, filters to builds requested for the specified use
        :return: Last build information
        """
        arguments = {}
        arguments['$top']=str(numBuilds)
        arguments['requestedFor']=requestedFor
        requestURL = "/" + project + "/_apis/build/builds/"
        return self.util.getRequest(requestURL, arguments)

    