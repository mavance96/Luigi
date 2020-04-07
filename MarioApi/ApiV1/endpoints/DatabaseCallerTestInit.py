import pyodbc


class DatabaseCallerTestInit():
    """"A class to set up the databases used by the Mario pipeline manager."""

    def __init__(self):
        """Initializes the databases connection."""
        server = 'tcp:projectspike.database.windows.net'
        database = 'ProjectsSpike'
        username = 'priort'
        password = 'SE4330team'
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = self.cnxn.cursor()


    def setup(self):
        self.cursor.execute("CREATE TABLE testDriveTypes("
                            "driveType varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("CREATE TABLE testEnvironments("
                            "environment varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("Create table testBuildIDs("
                            "buildID varchar(32) NOT NULL PRIMARY KEY, "
                            "driveType varchar(32), "
                            "Environment varchar(32), "
                            "unique (driveType, Environment), "
                            "foreign key (driveType) references testDriveTypes(driveType), "
                            "foreign key (Environment) references testEnvironments(environment));")
        # self.cursor.execute("CREATE TABLE testPipelineConfigurations("
        #                     "configID varchar(32) NOT NULL PRIMARY KEY, "
        #                     "buildID varchar(32), "
        #                     "pipelineID varchar(32), "
        #                     "agentID varchar(32), "
        #                     "globalFlag bit default 0, "
        #                     "foreign key (buildID) references testbuildIDs(buildID));")
        # self.cursor.execute("Create table testAccess("
        #                     "configID varchar(32) NOT NULL, "
        #                     "userName varchar(32) NOT NULL, "
        #                     "Primary Key (configID, userName), "
        #                     "Foreign Key (configID) references testPipelineConfigurations(configID));")
        # self.cursor.execute("Create table testArtifacts("
        #                     "configID varchar(32) NOT NULL, "
        #                     "artifactID varchar(32) NOT NULL,"
        #                     "Primary Key (configID, artifactID), "
        #                     "Foreign Key (configID) references testPipelineConfigurations(configID));")
        # self.cursor.execute("Create table testTags("
        #                     "configID varchar(32) NOT NULL, "
        #                     "tagName varchar(32) NOT NULL, "
        #                     "Primary Key (configID, tagName), "
        #                     "Foreign Key (configID) references testPipelineConfigurations(configID));")
        # self.cursor.execute("Create table testAbsoluteIDs( "
        #                     "absoluteID varchar(32) NOT NULL, "
        #                     "buildID varchar(32) NOT NULL, "
        #                     "Primary Key (absoluteID, buildiD),"
        #                     "Foreign Key (buildID) references testBuildIDs(buildID));")
        self.cursor.execute("Create table testPowerCards("
                            "powerCardID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (powerCardID)); ")
        self.cursor.execute("Create table testFirmwares("
                            "firmwareID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (firmwareID));")
        self.cursor.execute("Create table testApplications("
                            "applicationID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (applicationID));")
        self.cursor.execute("Create table testEmails("
                            "emailAddress varchar(256) NOT NULL,"
                            "name varchar(64),"
                            "Primary Key (emailAddress));")
        self.cursor.execute("CREATE TABLE testConfigurations("
                            "configID varchar(32) NOT NULL PRIMARY KEY, "
                            "buildID varchar(32), "
                            "applicationID varchar(32), "
                            "firmwareID varchar(32), "
                            "powerCardID varchar(32), "
                            "foreign key (buildID) references testBuildIDs(buildID), "
                            "foreign key (applicationID) references testApplications(applicationID), "
                            "foreign key (firmwareID) references testFirmwares(firmwareID), "
                            "foreign key (powerCardID) references testPowerCards(powerCardID));")
        self.cnxn.commit()

    def wipeTables(self):
        # self.cursor.execute("drop table testaccess;"
        #                     "drop table testtags;"
        #                     "drop table testartifacts;"
        #                     "drop table testpipelineconfigurations;"
        #                     "drop table testabsoluteids;"

        self.cursor.execute("drop table testConfigurations;"
                            "drop table testBuildids;"
                            "drop table testDriveTypes;"
                            "drop table testEnvironments;"
                            "drop table testApplications;"
                            "drop table testPowerCards;"
                            "drop table testFirmwares;"
                            "drop table testEmails;")
        self.cnxn.commit()

    def addDummyValues(self):
        self.cursor.execute("insert into testDriveTypes (driveType) values ('driveType1'), ('driveType2'), ('driveType3'), ('driveType4');")
        self.cursor.commit()
        self.cursor.execute("insert into testEnvironments (environment) values ('environment1'), ('environment2'), ('environment3'), ('environment4');")
        self.cnxn.commit()

        self.cursor.execute("insert into testbuildids (buildid, drivetype, environment) values ('build1' , 'driveType1', 'environment1'), ('build2' , 'driveType1', 'environment2'), "
                            "('build3' , 'driveType1', 'environment3'), ('build4' , 'driveType2', 'environment1'), ('build5' , 'driveType2', 'environment2'), "
                            "('build6' , 'driveType2', 'environment3'), ('build7' , 'driveType3', 'environment1'), ('build8' , 'driveType3', 'environment2'), "
                            "('build9' , 'driveType3', 'environment3');")
        # config that user has access to
        # self.cursor.execute(
        #     "insert into testPipelineConfigurations (configID, buildID, pipelineID, agentID) values "
        #     "('demoConfig1', 'build1', 'demoPipeline', 'demoAgent');")
        # self.cnxn.commit()
        # config that user does not have access to
        # self.cursor.execute(
        #     "insert into testPipelineConfigurations (configID, buildID, pipelineID, agentID, globalFlag) values "
        #     "('demoConfig2','build2', 'demoPipeline2', 'demoAgent2', 0);")
        # self.cnxn.commit()
        # config that user does not have access to, but is public
        # self.cursor.execute(
        #     "insert into testPipelineConfigurations (configID, buildID, pipelineID, agentID, globalFlag) values "
        #     "('demoConfig3','build3', 'demoPipeline3', 'demoAgent3', 1);")
        # self.cnxn.commit()

        # self.cursor.execute("insert into testtags (configID, tagName) values ('demoConfig1', 'tag1');")
        # self.cnxn.commit()

        # self.cursor.execute("insert into testaccess (configID, userName) values ('demoConfig1', 'Mike');")
        # self.cnxn.commit()

        # self.cursor.execute("insert into testartifacts (configID, artifactID) values ('demoConfig1', 'Artifact 1');")
        # self.cnxn.commit()
        # self.cursor.execute("insert into testartifacts (configID, artifactID) values ('demoConfig1', 'Artifact 2');")
        # self.cnxn.commit()
        # self.cursor.execute("insert into testartifacts (configID, artifactID) values ('demoConfig2', 'Artifact 2');")
        # self.cnxn.commit()
        self.cursor.execute("insert into testpowercards (powercardID, value) values ('demoPowerCard1', 'dummyValue');")
        self.cnxn.commit()
        self.cursor.execute("insert into testapplications (applicationID, value) values ('demoApplication1', 'dummyValue');")
        self.cnxn.commit()
        self.cursor.execute("insert into testfirmwares (firmwareID, value) values ('demoFirmware1', 'dummyValue');")
        self.cnxn.commit()
        # self.cursor.execute("insert into testabsoluteids (absoluteid, buildid) values ('abs1', 'build1'), ('abs2', 'build1');")
        # self.cnxn.commit()
        self.cursor.execute("insert into testEmails (emailAddress, name) values ('DoeJ@email.com', 'John Doe');")
        self.cnxn.commit()
        self.cursor.execute("insert into testConfigurations (configID, buildID, applicationID, firmwareID, powerCardID) values ('TestConfig', 'build1', 'demoApplication1', "
                            "'demoFirmware1', 'demoPowerCard1');")
        self.cnxn.commit()
