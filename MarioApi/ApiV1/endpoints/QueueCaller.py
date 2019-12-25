import json
import requests
from Utilities import Utilities

#This class calls Azure's Queue Api
class QueueCaller:

    #This method returns the Queue List, given the organization, in json string form.
    def get_listOfQueues(self, project):
        url = "/" + project + '/_apis/distributedtask/queues'
        return Utilities.getRequest(url)
