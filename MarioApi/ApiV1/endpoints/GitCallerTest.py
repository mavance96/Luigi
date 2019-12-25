import unittest
from GitCaller import GitCaller
from GitController import GitController
import json


class MyTestCase(unittest.TestCase):

    caller = GitCaller()
    repoListJson = {}
    branchListJson = {}

    def test_RepoList(self):
        jsonTestString = self.caller.getRepoList()
        assert jsonTestString == self.repoListJson

    def test_BranchList(self):
        jsonTestString = self.caller.getBranches()
        assert jsonTestString == self.branchListJson

if __name__ == '__main__':
    unittest.main()
