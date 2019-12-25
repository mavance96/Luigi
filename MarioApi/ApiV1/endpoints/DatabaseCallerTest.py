import unittest

from .TestDatabaseCaller import TestDatabaseCaller
from .DatabaseCallerTestInit import DatabaseCallerTestInit

dbCon = TestDatabaseCaller()
setupCon = DatabaseCallerTestInit()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        setupCon.setup()
        setupCon.addDummyValues()

    def tearDown(self):
        setupCon.wipeTables()

    def test_environment_get(self):
        expected = ['environment1','environment2','environment3','environment4']
        received = dbCon.environment_get()
        self.assertEqual(expected, received)

    def test_drive_types_get(self):
        expected = ['driveType1', 'driveType2', 'driveType3','driveType4']
        received = dbCon.drive_types_get()
        self.assertEqual(expected, received)

    def test_tags_get(self):
        expected = ['tag1']
        received = dbCon.tags_get('demoConfig1')
        self.assertEqual(expected, received)

    def test_tags_insert_new(self):
        dbCon.tags_insert('demoConfig2', 'tag2')
        received = dbCon.tags_get('demoConfig2')
        expected = ['tag2']
        self.assertEqual(expected, received)

    def test_tags_insert_same(self):
        inserted = dbCon.tags_insert('demoConfig1', 'tag1')
        received = dbCon.tags_get('demoConfig1')
        expected = ['tag1']
        self.assertEqual(False, inserted)
        self.assertEqual(expected, received)

    def test_tags_delete(self):
        dbCon.tags_delete('demoConfig2', 'tag2')
        received = dbCon.tags_get('demoConfig2')
        expected = []
        self.assertEqual(expected, received)

    def test_artifacts_get(self):
        received = dbCon.artifacts_get('demoConfig1')
        expected = ['Artifact 1', 'Artifact 2']
        self.assertEqual(expected, received)

    def test_artifacts_insert_new(self):
        dbCon.artifacts_insert('demoConfig3','Artifact 2')
        received = dbCon.artifacts_get('demoConfig3')
        expected = ['Artifact 2']
        self.assertEqual(expected, received)

    def test_artifacts_insert_same(self):
        inserted = dbCon.artifacts_insert('demoConfig1', 'Artifact 1')
        received = dbCon.artifacts_get('demoConfig1')
        expected = ['Artifact 1', 'Artifact 2']
        self.assertEqual(False, inserted)
        self.assertEqual(expected, received)

    def test_artifacts_delete(self):
        dbCon.artifacts_delete('demoConfig1', 'Artifact 1')
        received = dbCon.artifacts_get('demoConfig1')
        expected = ['Artifact 2']
        self.assertEqual(expected, received)

    def test_access_get(self):
        received = dbCon.access_get('Mike')
        expected = ['demoConfig1', 'demoConfig3']
        self.assertEqual(expected, received)

    def test_access_delete_public(self):
        dbCon.access_delete('demoConfig3','Mike')
        received = dbCon.access_get('Mike')
        expected = ['demoConfig1','demoConfig3']
        self.assertEqual(expected, received)

    def test_access_delete_private(self):
        dbCon.access_delete('demoConfig1','Mike')
        received = dbCon.access_get('Mike')
        expected = ['demoConfig3']
        self.assertEqual(expected, received)

    def test_access_insert_new(self):
        dbCon.access_insert('demoConfig1', 'Larry')
        received = dbCon.access_get('Larry')
        expected = ['demoConfig1', 'demoConfig3']
        self.assertEqual(expected, received)

    def test_access_insert_same(self):
        inserted = dbCon.access_insert('demoConfig1','Mike')
        received = dbCon.access_get('Mike')
        expected = ['demoConfig1', 'demoConfig3']
        self.assertEqual(False, inserted)
        self.assertEqual(expected, received)

    def test_pipeline_configs_get_names(self):
        received = dbCon.pipeline_configs_get_names()
        expected = ['demoConfig1','demoConfig2','demoConfig3']
        self.assertEqual(expected, received)

    def test_pipeline_configs_get(self):
        received = dbCon.pipeline_configs_get('demoConfig1')
        expected = {'configID' : 'demoConfig1',
                         'buildID' : 'build1',
                         'pipelineID' : 'demoPipeline',
                         'agentID' : 'demoAgent',
                         'driveType' : 'driveType1',
                         'environment' : 'environment1',
                         'globalFlag' : 'False'}
        self.assertEqual(expected, received)

    def test_pipeline_configs_update_int_flag(self):
        dbCon.pipeline_configs_update('demoConfig1', 'build1', 'demoPipeline', 'demoAgent2', 'driveType1', 'environment1', 1)
        received = dbCon.pipeline_configs_get('demoConfig1')
        expected = {'configID': 'demoConfig1',
                    'buildID': 'build1',
                    'pipelineID': 'demoPipeline',
                    'agentID': 'demoAgent2',
                    'driveType': 'driveType1',
                    'environment': 'environment1',
                    'globalFlag': 'True'}
        self.assertEqual(expected, received)

    def test_pipeline_configs_update_bool_flag(self):
        dbCon.pipeline_configs_update('demoConfig1', 'build1', 'demoPipeline', 'demoAgent2', 'driveType1',
                                      'environment1', True)
        received = dbCon.pipeline_configs_get('demoConfig1')
        expected = {'configID': 'demoConfig1',
                    'buildID': 'build1',
                    'pipelineID': 'demoPipeline',
                    'agentID': 'demoAgent2',
                    'driveType': 'driveType1',
                    'environment': 'environment1',
                    'globalFlag': 'True'}
        self.assertEqual(expected, received)

    def test_pipeline_configs_update_string_flag(self):
        dbCon.pipeline_configs_update('demoConfig1', 'build1', 'demoPipeline', 'demoAgent2', 'driveType1', 'environment1', 'True')
        received = dbCon.pipeline_configs_get('demoConfig1')
        expected = {'configID': 'demoConfig1',
                    'buildID': 'build1',
                    'pipelineID': 'demoPipeline',
                    'agentID': 'demoAgent2',
                    'driveType': 'driveType1',
                    'environment': 'environment1',
                    'globalFlag': 'True'}
        self.assertEqual(expected, received)

    def test_pipeline_configs_insert_new(self):
        dbCon.pipeline_configs_insert('testConfig1', 'build1', 'demoPipeline', 'demoAgent1', 'driveType1', 'environment1', 'True')
        received = dbCon.pipeline_configs_get('testConfig1')
        expected = {'configID': 'testConfig1',
                    'buildID': 'build1',
                    'pipelineID': 'demoPipeline',
                    'agentID': 'demoAgent1',
                    'driveType': 'driveType1',
                    'environment': 'environment1',
                    'globalFlag': 'True'}
        self.assertEqual(expected, received)

    def test_pipeline_configs_insert_same(self):
        inserted = dbCon.pipeline_configs_insert('demoConfig1', 'build1', 'demoPipeline', 'demoAgent1', 'driveType1', 'environment1', 'True')
        received = dbCon.pipeline_configs_get_names()
        expected = ['demoConfig1','demoConfig2','demoConfig3']
        self.assertEqual(False, inserted)
        self.assertEqual(expected, received)

    def test_pipeline_configs_delete(self):
        dbCon.pipeline_configs_delete('demoConfig1')
        received = dbCon.pipeline_configs_get_names()
        expected = ['demoConfig2', 'demoConfig3']
        self.assertEqual(expected, received)

    def test_buildIDs_get(self):
        received = dbCon.buildIDs_get('driveType3', 'environment3')
        expected = 'build9'
        self.assertEqual(expected, received)

    def test_absoluteIDs_get(self):
        received = dbCon.absoluteIDs_get('build1')
        expected = ['abs1', 'abs2']
        self.assertEqual(expected, received)

    def test_buildIDs_getAll(self):
        received = dbCon.buildIDs_getAll()
        expected = ['build1','build2','build3','build4','build5','build6','build7','build8','build9']
        self.assertEqual(expected, received)

    def test_buildIDs_insert(self):
        received = dbCon.buildIDs_insert('build9', 'driveType3', 'environment3')
        expected = False
        self.assertEqual(expected, received)
        received = dbCon.buildIDs_insert('build10', 'driveType3', 'environment3')
        expected = False
        self.assertEqual(expected, received)
        received = dbCon.buildIDs_insert('build9', 'driveType4', 'environment4')
        expected = False
        self.assertEqual(expected, received)
        received = dbCon.buildIDs_insert('build10', 'driveType4', 'environment4')
        expected = True
        self.assertEqual(expected, received)

if __name__ == '__main__':
    unittest.main()
