from Utilities import Utilities

class ArtifactsCaller:

    def __init__(self, util):
        self.util = util

    def get_ListOfArtifacts(self, project, build_id):
        """
        Returns a list of artifacts for that specific build
        """
        requestUrl = "/" + project + "/_apis/build/builds/" + str(build_id) + "/artifacts"
        return util.getRequest(requestUrl)

    def get_ArtifactByName(self, project, build_id, artifact_name):
        """
        Returns a specified artifact object, given the name.
        """
        requestUrl = "/" + project + "/_apis/build/builds/" + str(build_id) + "/artifacts?artifactName=" + str(artifact_name)
        return util.getRequest(requestUrl)





