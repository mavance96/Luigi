from django.test import TestCase
from endpoints import ConfigurationController
from UnitTests.stubs.ConfigurationControllerStubs import ConfigurationControllerStubs

class Tests(TestCase):

    def testBranchNames(self):
        print("In test.py")
        branchResponse = ConfigurationControllerStubs.TwoBranchesResponse()
        expected = ["develop", "master"]
        # result = ConfigurationController.parseBranchData(branchResponse)
        # self.assertEqual(expected,result)