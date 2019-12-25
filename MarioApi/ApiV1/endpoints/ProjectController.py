import json
from Utilities import Utilities

class ProjectController:

    def __init__(self, proCaller):
        self.proCaller = proCaller
        self.util = Utilities()
        
    def getProjectList(self, organization):
        jsonString = self.proCaller.listAPICaller(organization)
        return self.util.jsonString(jsonString)