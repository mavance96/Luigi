import json
import requests

#This class calls Azure's Project Api
class ProjectCaller:

    def __init__(self, util):
        self.util = util
    

    #This method returns the Project List, given the organization, in json string form.
    def get_listOfProjects(self):
        url = '/_apis/projects'

        return self.util.getRequest(url)
        
