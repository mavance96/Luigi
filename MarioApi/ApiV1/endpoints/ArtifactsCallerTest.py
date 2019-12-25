from ArtifactsCaller import ArtifactsCaller
import unittest

class ArtifactsTest(unittest.TestCase):

    def setUp(self):
        self.buildTestNumber = 1
        self.project = "SE4330-Mario"
        self.artifactTestName = "nameThatNoArtifactWillProbablyHold"
        self.caller = ArtifactsCaller()

    def test_ArtifactsList(self):
        test = self.caller.get_ListOfArtifacts(self.project, self.buildTestNumber)
        assert test

    def test_getArtifact(self):
        test = self.caller.get_ArtifactByName(self.project, self.buildTestNumber, self.artifactTestName)
        assert test == None

if __name__ == '__main__':
    unittest.main()


