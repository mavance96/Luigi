from GitCaller import GitCaller
import json

class GitCallerStub(GitCaller):

    repoListJson = {
          "count": 2,
          "value": [
            {
              "id": "5febef5a-833d-4e14-b9c0-14cb638f91e6",
              "name": "AnotherRepository",
              "url": "https://dev.azure.com/fabrikam/_apis/git/repositories/5febef5a-833d-4e14-b9c0-14cb638f91e6",
              "project": {
                "id": "6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                "name": "Fabrikam-Fiber-Git",
                "url": "https://dev.azure.com/fabrikam/_apis/projects/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                "state": "wellFormed"
              },
              "remoteUrl": "https://dev.azure.com/fabrikam/Fabrikam-Fiber-Git/_git/AnotherRepository"
            },
            {
              "id": "278d5cd2-584d-4b63-824a-2ba458937249",
              "name": "Fabrikam-Fiber-Git",
              "url": "https://dev.azure.com/fabrikam/_apis/git/repositories/278d5cd2-584d-4b63-824a-2ba458937249",
              "project": {
                "id": "6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                "name": "Fabrikam-Fiber-Git",
                "url": "https://dev.azure.com/fabrikam/_apis/projects/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c",
                "state": "wellFormed"
              },
              "defaultBranch": "refs/heads/master",
              "remoteUrl": "https://dev.azure.com/fabrikam/_git/Fabrikam-Fiber-Git"
            }
          ]
        }

    branchListJson = {
          "value": [
            {
              "name": "refs/remotes/origin/master",
              "objectId": "ffe9cba521f00d7f60e322845072238635edb451",
              "creator": {
                "displayName": "Normal Paulk",
                "url": "https://vssps.dev.azure.com/fabrikam/_apis/Identities/ac5aaba6-a66a-4e1d-b508-b060ec624fa9",
                "_links": {
                  "avatar": {
                    "href": "https://dev.azure.com/fabrikam/_apis/GraphProfile/MemberAvatars/aad.YmFjMGYyZDctNDA3ZC03OGRhLTlhMjUtNmJhZjUwMWFjY2U5"
                  }
                },
                "id": "ac5aaba6-a66a-4e1d-b508-b060ec624fa9",
                "uniqueName": "dev@mailserver.com",
                "imageUrl": "https://dev.azure.com/fabrikam/_api/_common/identityImage?id=ac5aaba6-a66a-4e1d-b508-b060ec624fa9",
                "descriptor": "aad.YmFjMGYyZDctNDA3ZC03OGRhLTlhMjUtNmJhZjUwMWFjY2U5"
              },
              "url": "https://dev.azure.com/fabrikam/7484f783-66a3-4f27-b7cd-6b08b0b077ed/_apis/git/repositories/d3d1760b-311c-4175-a726-20dfc6a7f885/refs?filter=remotes%2Forigin%2Fmaster"
            },
            {
              "name": "refs/tags/v0.1",
              "objectId": "917131a709996c5cfe188c3b57e9a6ad90e8b85c",
              "creator": {
                "displayName": "Normal Paulk",
                "url": "https://vssps.dev.azure.com/fabrikam/_apis/Identities/ac5aaba6-a66a-4e1d-b508-b060ec624fa9",
                "_links": {
                  "avatar": {
                    "href": "https://dev.azure.com/fabrikam/_apis/GraphProfile/MemberAvatars/aad.YmFjMGYyZDctNDA3ZC03OGRhLTlhMjUtNmJhZjUwMWFjY2U5"
                  }
                },
                "id": "ac5aaba6-a66a-4e1d-b508-b060ec624fa9",
                "uniqueName": "dev@mailserver.com",
                "imageUrl": "https://dev.azure.com/fabrikam/_api/_common/identityImage?id=ac5aaba6-a66a-4e1d-b508-b060ec624fa9",
                "descriptor": "aad.YmFjMGYyZDctNDA3ZC03OGRhLTlhMjUtNmJhZjUwMWFjY2U5"
              },
              "url": "https://dev.azure.com/fabrikam/7484f783-66a3-4f27-b7cd-6b08b0b077ed/_apis/git/repositories/d3d1760b-311c-4175-a726-20dfc6a7f885/refs?filter=tags%2Fv0.1"
            }
          ],
          "count": 2
        }

    def repoListCall(self, organization, projectId):
        return json.dumps(self.repoListJson)

    def branchListCall(self, organization, projectId, repositoryName):
        return json.dumps(self.branchListJson)