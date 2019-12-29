class ConfigurationControllerStubs:

    def TwoBranchesResponse():
        return """
        {
            "value": [
                {
                    "name": "refs/heads/develop",
                    "objectId": "61702ac842c883f8b09fcfeb531ab5908419c18f",
                    "creator": {
                        "displayName": "Mitchell Vance",
                        "url": "https://spsprodcus3.vssps.visualstudio.com/A42eb98c5-40e5-4d7c-ace6-4a4c7f59ccd3/_apis/Identities/6ebd5679-c3b2-6d41-9f84-9ff429d29224",
                        "_links": {
                            "avatar": {
                                "href": "https://dev.azure.com/adasupershi/_apis/GraphProfile/MemberAvatars/msa.NmViZDU2NzktYzNiMi03ZDQxLTlmODQtOWZmNDI5ZDI5MjI0"
                            }
                        },
                        "id": "6ebd5679-c3b2-6d41-9f84-9ff429d29224",
                        "uniqueName": "mitchell117@live.com",
                        "imageUrl": "https://dev.azure.com/adasupershi/_api/_common/identityImage?id=6ebd5679-c3b2-6d41-9f84-9ff429d29224",
                        "descriptor": "msa.NmViZDU2NzktYzNiMi03ZDQxLTlmODQtOWZmNDI5ZDI5MjI0"
                    },
                    "url": "https://dev.azure.com/adasupershi/d5a809eb-7f7b-45cd-ae75-8360371b0bf2/_apis/git/repositories/8b4912d0-116f-42eb-b5ea-71b3cdbd8f80/refs?filter=heads%2FDevelop"
                },
                {
                    "name": "refs/heads/master",
                    "objectId": "49c38652b2d335a43e380acdb040ab6e4629f006",
                    "creator": {
                        "displayName": "Yan Shi",
                        "url": "https://spsprodcus3.vssps.visualstudio.com/A42eb98c5-40e5-4d7c-ace6-4a4c7f59ccd3/_apis/Identities/f4dfe6e3-1e36-65f7-840d-1988ac451bca",
                        "_links": {
                            "avatar": {
                                "href": "https://dev.azure.com/adasupershi/_apis/GraphProfile/MemberAvatars/msa.ZjRkZmU2ZTMtMWUzNi03NWY3LTg0MGQtMTk4OGFjNDUxYmNh"
                            }
                        },
                        "id": "f4dfe6e3-1e36-65f7-840d-1988ac451bca",
                        "uniqueName": "adasuper.shi@gmail.com",
                        "imageUrl": "https://dev.azure.com/adasupershi/_api/_common/identityImage?id=f4dfe6e3-1e36-65f7-840d-1988ac451bca",
                        "descriptor": "msa.ZjRkZmU2ZTMtMWUzNi03NWY3LTg0MGQtMTk4OGFjNDUxYmNh"
                    },
                    "url": "https://dev.azure.com/adasupershi/d5a809eb-7f7b-45cd-ae75-8360371b0bf2/_apis/git/repositories/8b4912d0-116f-42eb-b5ea-71b3cdbd8f80/refs?filter=heads%2Fmaster"
                }
            ],
            "count": 2
        }
        """

    def OneBranchResponse():
        return """
        {
            "value": [
                {
                    "name": "refs/heads/develop",
                    "objectId": "61702ac842c883f8b09fcfeb531ab5908419c18f",
                    "creator": {
                        "displayName": "Mitchell Vance",
                        "url": "https://spsprodcus3.vssps.visualstudio.com/A42eb98c5-40e5-4d7c-ace6-4a4c7f59ccd3/_apis/Identities/6ebd5679-c3b2-6d41-9f84-9ff429d29224",
                        "_links": {
                            "avatar": {
                                "href": "https://dev.azure.com/adasupershi/_apis/GraphProfile/MemberAvatars/msa.NmViZDU2NzktYzNiMi03ZDQxLTlmODQtOWZmNDI5ZDI5MjI0"
                            }
                        },
                        "id": "6ebd5679-c3b2-6d41-9f84-9ff429d29224",
                        "uniqueName": "mitchell117@live.com",
                        "imageUrl": "https://dev.azure.com/adasupershi/_api/_common/identityImage?id=6ebd5679-c3b2-6d41-9f84-9ff429d29224",
                        "descriptor": "msa.NmViZDU2NzktYzNiMi03ZDQxLTlmODQtOWZmNDI5ZDI5MjI0"
                    },
                    "url": "https://dev.azure.com/adasupershi/d5a809eb-7f7b-45cd-ae75-8360371b0bf2/_apis/git/repositories/8b4912d0-116f-42eb-b5ea-71b3cdbd8f80/refs?filter=heads%2FDevelop"
                }
            ],
            "count": 1
        }
        """