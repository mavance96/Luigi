import json


class BuildDefinitionCaller:
    def __init__(self, util):
        self.util = util

    def get_buildDefinitions(self, project, params={}):
        """
        Returns a list of build definitions in the project matching optional parameters
        :param project: project being checked
        :param params: optional filtering parameters
        :return: the results of the request
        """
        requestURL = "/" + project + "/_apis/build/definitions"
        return self.util.getRequest(requestURL, params)

    def get_buildDefinitionMetrics(self, project, definitionID, params={}):
        """
        Returns a json object containing metric data for the pipeline
        :param project: project being checked
        :param definitionID: id for pipeline to get metrics from
        :param params: optional parameters passed to api call
        :return: result of api call
        """
        requestURL = "/" + project + "/_apis/build/definitions/" + str(definitionID) + "/metrics"
        return self.util.getRequest(requestURL, params)