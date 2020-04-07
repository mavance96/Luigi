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
        received = dbCon.environments_get()
        self.assertEqual(expected, received)

    def test_environment_insert(self):
        expected = True
        received = dbCon.environments_insert('newEnv')
        self.assertEqual(expected, received)

    def test_drive_types_get(self):
        expected = ['driveType1', 'driveType2', 'driveType3','driveType4']
        received = dbCon.drive_types_get()
        self.assertEqual(expected, received)

    def test_drive_types_insert(self):
        expected = True
        received = dbCon.drive_types_insert('newDT')
        self.assertEqual(expected, received)

    def test_buildIDs_get(self):
        received = dbCon.buildIDs_get('driveType3', 'environment3')
        expected = 'build9'
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

    def test_applications_insert(self):
        received = dbCon.applications_insert('demoApplication1', 'dummyValue')
        expected = False
        self.assertEqual(expected, received)
        received = dbCon.applications_insert('demoApplication2', 'dummyValue')
        expected = True
        self.assertEqual(expected, received)

    def test_applications_delete(self):
        dbCon.applications_delete('demoApplication1')
        received = dbCon.applications_get_names()
        expected = []
        self.assertEqual(expected, received)

    def test_applications_get_names(self):
        received = dbCon.applications_get_names()
        expected = ['demoApplication1']
        self.assertEqual(expected, received)

    def test_applications_get(self):
        received = dbCon.applications_get('demoApplication1')
        expected = {'applicationID': 'demoApplication1',
                    'value': 'dummyValue'}
        self.assertEqual(expected, received)

    def test_firmwares_insert(self):
        received = dbCon.firmwares_insert('demoFirmware1', 'dummyValue')
        expected = False
        self.assertEqual(expected, received)
        received = dbCon.firmwares_insert('demoFirmware2', 'dummyValue')
        expected = True
        self.assertEqual(expected, received)

    def test_firmwares_delete(self):
        dbCon.firmwares_delete('demoFirmware1')
        received = dbCon.firmwares_get_names()
        expected = []
        self.assertEqual(expected, received)

    def test_firmwares_get_names(self):
        received = dbCon.firmwares_get_names()
        expected = ['demoFirmware1']
        self.assertEqual(expected, received)

    def test_firmwares_get(self):
        received = dbCon.firmwares_get('demoFirmware1')
        expected = {'firmwareID': 'demoFirmware1',
                    'value': 'dummyValue'}
        self.assertEqual(expected, received)

    def test_powercards_insert(self):
        received = dbCon.powercards_insert('demoPowerCard1', 'dummyValue')
        expected = False
        self.assertEqual(expected, received)
        received = dbCon.powercards_insert('demoPowerCard2', 'dummyValue')
        expected = True
        self.assertEqual(expected, received)

    def test_powercards_delete(self):
        dbCon.powercards_delete('demoPowerCard1')
        received = dbCon.powercards_get_names()
        expected = []
        self.assertEqual(expected, received)

    def test_powercards_get_names(self):
        received = dbCon.powercards_get_names()
        expected = ['demoPowerCard1']
        self.assertEqual(expected, received)

    def test_powercards_get(self):
        received = dbCon.powercards_get('demoPowerCard1')
        expected = {'powercardID': 'demoPowerCard1',
                    'value': 'dummyValue'}
        self.assertEqual(expected, received)

    def test_drive_types_get_by_environment(self):
        received = dbCon.drive_types_get_by_environment('environment1')
        expected = ['driveType1', 'driveType2', 'driveType3']
        self.assertEqual(expected, received)

    def test_environments_get_by_environment(self):
        received = dbCon.environments_get_by_drive_type('driveType1')
        expected = ['environment1', 'environment2', 'environment3']
        self.assertEqual(expected, received)

    def test_emails_insert(self):
        received = dbCon.emails_insert('DoeJa@email.com', 'Jane Doe')
        expected = True
        self.assertEqual(expected, received)

    def test_emails_getAll(self):
        received = dbCon.emails_getAll()
        expected = [('DoeJ@email.com', 'John Doe')]
        self.assertEqual(expected, received)

    def test_emails_delete(self):
        received = dbCon.emails_delete('DoeJ@email.com')
        expected = True
        self.assertEqual(expected, received)

    def test_emails_insert_getAll(self):
        received = dbCon.emails_insert('DoeJa@email.com', 'Jane Doe')
        expected = True
        self.assertEqual(expected, received)

        received2 = dbCon.emails_getAll()
        expected2 = [('DoeJa@email.com', 'Jane Doe'),('DoeJ@email.com', 'John Doe')]
        self.assertEqual(expected2, received2)

    def test_configurations_insert(self):
        received = dbCon.configurations_insert('newConfig', 'build2', 'demoApplication1', 'demoFirmware1', 'demoPowerCard1')
        expected = True
        self.assertEqual(expected, received)

    def test_configurations_get_names(self):
        received = dbCon.configurations_get_names()
        expected = ['TestConfig']
        self.assertEqual(expected, received)

    def test_configurations_get(self):
        received = dbCon.configurations_get('TestConfig')
        expected = ['build1', 'driveType1', 'environment1', 'demoApplication1', 'demoFirmware1', 'demoPowerCard1']
        self.assertEqual(expected, received)

    def test_configurations_update(self):
        received = dbCon.configurations_update('TestConfig', 'build2', 'demoApplication1', 'demoFirmware1', 'demoPowerCard1')
        expected = True
        self.assertEqual(expected, received)

    def test_configurations_delete(self):
        received = dbCon.configurations_delete('TestConfig')
        expected = True
        self.assertEqual(expected, received)

if __name__ == '__main__':
    unittest.main()
