import json

" Calls run caller"
class TestRunCaller:
    def __init__(self, util):
        self.util = util
    #This fucntion calls run endpoint by JP
    def get_list_of_runs(self, project, build_id, params={}):
        """
        Returns a build and its information, given an id
        :param build_id:  Your "absolute" build id
        :return: Build information
        """
        #https://dev.azure.com/adasupershi/se4330-mario/_apis/test/runs?buildUri=vstfs:///Build/Build/766&api-version=5.1
       # requestURL = "/" + project + "/_apis/test/runs/" + 'vstfs:///Build/Build/' + str(build_id)
        params["buildUri"] = ("vstfs:///Build/Build/" + str(build_id))
        requestURL = "/" + project + "/_apis/test/runs/"

        return self.util.getRequest(requestURL, params)
