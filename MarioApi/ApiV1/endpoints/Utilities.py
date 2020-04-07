import json
import requests


# Utility Class containing common methods for API Callers and Controllers
class Utilities:

    def __init__(self, token, organization):
        self.token = token
        self.organization = organization

    def getRequest(self, url, args={}):
        fullURL = self.__getURL(url, args)
        response = requests.get(url=fullURL, headers=self.__getHeader())
        if response.status_code == 200:
            return json.loads(json.dumps(response.content.decode('utf-8')))
        return response.status_code

    def postRequest(self, url, data, args=dict()):
        fullURL = self.__getURL(url, args)
        response = requests.post(url=fullURL, data=data, headers=self.__getHeader())
        return response.status_code
    
    #Do we need this?
    def deleteRequest(self, url, args={}):
        fullURL = self.__getURL(url, args)
        response = requests.delete(url=fullURL, headers=self.__getHeader())
        return response.status_code

    def __getHeader(self):
        return {"Authorization": "Bearer {}".format(self.token), "Content-Type": "application/json"}

    def __getURL(self, url, args):
        fullURL = "https://dev.azure.com/" + self.organization + url + "?api-version=5.1-preview"
        for key, value in args.items():
            fullURL = fullURL + "&" + key + "=" + value
        return fullURL

    def checkParams(self, jsonbody, optionalParams):
        """
        This goes through a json object and checks each
        parameter specified in the optionalParams list of strings.
        If the parameter does not exist, create one with a
        value of None.
        Parameters:
            jsonbody (json) : The json object to edit.
            optionalParams (str []) : The list of parameters to check
        """
        for parameter in optionalParams:
            try:
                jsonbody[parameter]
            except:
                jsonbody[parameter] = None

