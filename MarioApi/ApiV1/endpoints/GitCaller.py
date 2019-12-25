import json
import requests
from .Utilities import Utilities

#This class calls Azure's Git Api
class GitCaller:
       
    def __init__(self, util):
        self.util = util
    
    #This method returns the Repo List given the organization and project ID, in json string form.
    def get_listOfRepos(self, project):
        url = "/" + project + '/_apis/git/repositories'
        return self.util.getRequest(url)


    #This method returns the branch list, given the organization, project ID and Repo Name, in json string form.
    def get_listOfBranches(self, project, repo):
        url = "/" + project + '/_apis/git/repositories/{0}/refs'.format(
            repo)
        return self.util.getRequest(url)

