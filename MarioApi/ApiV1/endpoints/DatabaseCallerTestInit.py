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

        # Creating new tables
        self.cursor.execute("CREATE TABLE DriveTypes("
                       "driveType varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("CREATE TABLE Environments("
                       "environment varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("CREATE TABLE PipelineConfigurations("
                       "configID varchar(32) NOT NULL PRIMARY KEY, "
                       "buildID varchar(32), "
                       "pipelineID varchar(32), "
                       "agentID varchar(32), "
                       "driveType varchar(32), "
                       "environment varchar(32), "
                       "globalFlag bit default 0, "
                       "foreign key (driveType) references DriveTypes(driveType), "
                       "foreign key (environment) references Environments(environment));")
        self.cursor.execute("Create table Access("
                       "configID varchar(32) NOT NULL, "
                       "userName varchar(32) NOT NULL, "
                       "Primary Key (configID, userName), "
                       "Foreign Key (configID) references PipelineConfigurations(configID));")
        self.cursor.execute("Create table Artifacts("
                       "configID varchar(32) NOT NULL, "
                       "artifactID varchar(32) NOT NULL,"
                       "Primary Key (configID, artifactID), "
                       "Foreign Key (configID) references PipelineConfigurations(configID));")
        self.cursor.execute("Create table Tags("
                       "configID varchar(32) NOT NULL, "
                       "tagName varchar(32) NOT NULL, "
                       "Primary Key (configID, tagName), "
                       "Foreign Key (configID) references PipelineConfigurations(configID));")
        self.cnxn.commit()

    def wipeTables(self):
        self.cursor.execute("drop table access;"
                            "drop table tags;"
                            "drop table artifacts;"
                            "drop table pipelineconfigurations;"
                            "drop table DriveTypes;"
                            "drop table Environments;")
        self.cnxn.commit()

    def addDummyValues(self):
        self.cursor.execute("insert into DriveTypes (driveType) values ('driveType1'), ('driveType2'), ('driveType3');")
        self.cursor.execute(
            "insert into Environments (environment) values ('environment1'), ('environment2'), ('environment3');")
        # config that user has access to
        self.cursor.execute(
            "insert into PipelineConfigurations (configID, buildID, pipelineID, agentID, driveType, environment) values "
            "('demoConfig1', 'demoBuild', 'demoPipeline', 'demoAgent', 'driveType1', 'environment1');")
        self.cnxn.commit()
        # config that user does not have access to
        self.cursor.execute(
            "insert into PipelineConfigurations (configID, buildID, pipelineID, agentID, driveType, environment, globalFlag) values "
            "('demoConfig2','demoBuild2', 'demoPipeline2', 'demoAgent2', 'driveType2', 'environment2', 0);")
        self.cnxn.commit()
        # config that user does not have access to, but is public
        self.cursor.execute(
            "insert into PipelineConfigurations (configID, buildID, pipelineID, agentID, driveType, environment, globalFlag) values "
            "('demoConfig3','demoBuild3', 'demoPipeline3', 'demoAgent3', 'driveType3', 'environment3', 1);")
        self.cnxn.commit()

        self.cursor.execute("insert into tags (configID, tagName) values ('demoConfig1', 'tag1');")
        self.cnxn.commit()

        self.cursor.execute("insert into access (configID, userName) values ('demoConfig1', 'Mike');")
        self.cnxn.commit()

        self.cursor.execute("insert into artifacts (configID, artifactID) values ('demoConfig1', 'Artifact 1');")
        self.cnxn.commit()
        self.cursor.execute("insert into artifacts (configID, artifactID) values ('demoConfig1', 'Artifact 2');")
        self.cnxn.commit()
        self.cursor.execute("insert into artifacts (configID, artifactID) values ('demoConfig2', 'Artifact 2');")
        self.cnxn.commit()