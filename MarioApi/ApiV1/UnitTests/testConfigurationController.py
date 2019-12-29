from django.test import TestCase
from .stubs.ConfigurationControllerStubs import ConfigurationControllerStubs
from endpoints import ConfigurationController

class ConfigurationControllerTests(TestCase):

    def testMultipleBranchesInList(self):
        print("Testing multiple branch names...")
        branchResponse = ConfigurationControllerStubs.TwoBranchesResponse()
        expected = ["develop", "master"]
        result = ConfigurationController.parseBranchData(branchResponse)
        self.assertEqual(expected,result)

    def testOneBranchInList(self):
        print("Testing one branch in list...")
        branchResponse = ConfigurationControllerStubs.OneBranchResponse()
        expected = ["develop"]
        result = ConfigurationController.parseBranchData(branchResponse)
        self.assertEqual(expected,result)