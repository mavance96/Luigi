from BuildsCaller import BuildsCaller
import unittest

class BuildsCallerTest(unittest.TestCase):

    def setUp(self):
        self.project = "SE4330-Mario"
        self.caller = BuildsCaller()
        self.faultyBuildTestNumber = -1
        self.buildTestNumber = 1
        self.logTestNumber = 1

    def test_getBuildByID(self):
        test = self.caller.get_buildByID(self.project, self.faultyBuildTestNumber)
        assert test == None

    def test_listOfBuilds(self):
        test = self.caller.get_listOfBuilds(self.project)
        assert test

    def test_queueBuild(self):
        test = self.caller.queue_build(self.project, self.buildTestNumber)
        assert test

    def test_deleteBuild(self):
        test = self.caller.delete_build(self.project, self.buildTestNumber)
        assert test

    def test_getBuildLogs(self):
        test = self.caller.get_buildLogs(self.project, self.buildTestNumber)
        assert test

    def test_getBuildLog(self):
        test = self.caller.get_buildLog(self.project, self.buildTestNumber, self.logTestNumber)
        assert test

if __name__ == '__main__':
    unittest.main()
