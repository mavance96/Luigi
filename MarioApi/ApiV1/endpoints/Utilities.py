import json
import requests

#Utility Class containing common methods for API Callers and Controllers
class Utilities:
    
    def __init__(self, token, organization):
        self.token = token
        self.organization = organization

    def getRequest(self, url, args=dict()):
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
    def deleteRequest(self, url, args=dict()):
        fullURL = self.__getURL(url, args)
        response = requests.delete(url=fullURL, headers=self.__getHeader())
        return response.status_code
        
    def __getHeader(self):
        return {"Authorization": "Bearer {}".format(self.token), "Content-Type": "application/json"}
        
    def __getURL(self, url, args):
        fullURL = "https://dev.azure.com/" + self.organization + url + "?api-version=5.1-preview"
        for key, value in args:
            fullURL = fullURL + "&" + key + "=" + value
        return fullURL
