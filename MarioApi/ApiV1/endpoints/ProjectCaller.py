import json
import requests
from Utilities import Utilities

#This class calls Azure's Project Api
class ProjectCaller:

    #This method returns the Project List, given the organization, in json string form.
    def get_listOfProjects(self):
        url = '/_apis/projects'
        return Utilities.getRequest(url)
