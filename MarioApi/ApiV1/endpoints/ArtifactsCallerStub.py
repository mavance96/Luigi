from ArtifactsCaller import ArtifactsCaller
import json

class ArtifactsCallerStub(ArtifactsCaller):

    artifactsListJSON = {
        "count": 1,
        "value": [
            {
                "buildId": 1,
                "project": {
                    "id": "6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                    "name": "Fabrikam-Fiber-Git",
                    "url": "https://dev.azure.com/fabrikam/_apis/projects/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                    "state": "wellFormed"
                },
            }
        ]
    }

    artifactJSON = {
        "value": [
            {
                "buildId": 1,
                "artifactName": "drop",
                "project": {
                    "id": "6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                    "name": "Fabrikam-Fiber-Git",
                    "url": "https://dev.azure.com/fabrikam/_apis/projects/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                    "state": "wellFormed"
                }
            }
        ]
    }

    def artifactsListJSONCall(self):
        return json.dumps(self.artifactsListJSON)

    def artifactsJSONCall(self):
        return json.dumps(self.artifactJSON)