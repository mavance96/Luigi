import json
from Utilities import Utilities

class QueueController:
    
    def __init__(self, queueCaller):
        self.queueCaller = queueCaller
        self.util = Utilities()
        
    def getQueueList(self, organization):
        jsonString = self.queueCaller.queueList(organization)
        return self.util.jsonString(jsonString)