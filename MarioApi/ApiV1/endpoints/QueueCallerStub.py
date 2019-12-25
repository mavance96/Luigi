from QueueCaller import QueueCaller
import json


class QueueCallerStub(QueueCaller):

    jsonQueueTest = {
        "count": 2,
        "value":
            [
                {
                    "id": 1000,
                    "projectId": "eb6e4656-77fc-42a1-9181-4c6d8e9da5d1",
                    "name": "Fabrikam-Fiber-TFVC",
                    "isHosted": True,
                    "poolType":
                    {
                        "automation": "Successful",
                        "deployment": "Successful",
                    },
                },

                {
                    "id": 2000,
                    "projectId": "6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                    "name": "Fabrikam-Fiber-Git",
                    "isHosted": True,
                    "poolType":
                    {
                        "automation": "Successful",
                        "deployment": "Successful",
                    },
                }
            ]
        }

    def queueList(self, organization):
        return json.dumps(self.jsonQueueTest)