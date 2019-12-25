import json
from Utilities import Utilities

class GitController:

    def __init__(self, caller):
        self.caller = caller
        self.util = Utilities()
        
    def getRepoList(self, organization, projectId):
        jsonString = self.caller.repoListCall(organization,projectId)
        return self.util.jsonString(jsonString)

    def getBranches(self, organization, projectId, repositoryName):
        jsonString = self.caller.branchListCall(organization, projectId, repositoryName)
        return self.util.jsonString(jsonString)

