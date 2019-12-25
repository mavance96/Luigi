import unittest
from QueueCaller import QueueCaller
import json


class MyTestCase(unittest.TestCase):
    
    caller = QueueCaller()
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


    def test_queueList(self):
        queueList = self.caller.queueList(json.dumps(self.jsonListTest))
        queueMap = queueList[0]
        assert queueMap['id'] == 1000
        assert queueMap['projectId'] == "eb6e4656-77fc-42a1-9181-4c6d8e9da5d1"
        assert queueMap['name'] == "Fabrikam-Fiber-TFVC"
        assert queueMap['isHosted'] == True
        assert queueMap['poolType'] == {
                        "automation": "Successful",
                        "deployment": "Successful",
                    }        

if __name__ == '__main__':
    unittest.main()
