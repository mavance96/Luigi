import pyodbc


class DatabaseInit():
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
        self.cursor.execute("Create table BuildIDs("
                            "buildID varchar(32) NOT NULL PRIMARY KEY, "
                            "driveType varchar(32), "
                            "testEnvironment varchar(32), "
                            "unique (driveType, testEnvironment), "
                            "foreign key (driveType) references DriveTypes(driveType), "
                            "foreign key (testEnvironment) references Environments(environment));")
        self.cursor.execute("CREATE TABLE PipelineConfigurations("
                        "configID varchar(32) NOT NULL PRIMARY KEY, "
                        "buildID varchar(32), "
                        "pipelineID varchar(32), "
                        "agentID varchar(32), "
                        "driveType varchar(32), "
                        "environment varchar(32), "
                        "globalFlag bit default 0, "
                        "foreign key (driveType) references DriveTypes(driveType), "
                        "foreign key (environment) references Environments(environment), "
                        "foreign key (buildID) references buildIDs(buildID));")
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
        self.cursor.execute("Create table AbsoluteIDs( "
                            "absoluteID varchar(32) NOT NULL, "
                            "buildID varchar(32) NOT NULL, "
                            "Primary Key (absoluteID, buildiD),"
                            "Foreign Key (buildID) references BuildIDs(buildID));")
        self.cnxn.commit()