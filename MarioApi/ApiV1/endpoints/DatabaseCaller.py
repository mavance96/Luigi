import pyodbc


class DatabaseCaller():
    """"A class to manage the databases used by the Mario pipeline manager."""

    def __init__(self):
        """Initializes the databases connection."""
        server = 'tcp:projectspike.database.windows.net'
        database = 'ProjectsSpike'
        username = 'priort'
        password = 'SE4330team'
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = self.cnxn.cursor()

    def pipeline_configs_update(self, configID, buildID, pipelineID, agentID, driveType, environment, globalFlag):
        """Updates the PipelineConfigurations SQL table."""
        try:
            #Converts globalFlag to a string if it's being represented by 0 or 1
            if (type(globalFlag) == 'int' or type(globalFlag) == 'bool'):
                if globalFlag == 1 or globalFlag == True:
                    globalFlag = 'True'
                if globalFlag == 0 or globalFlag == False:
                    globalFlag = 'False'
            #Calls SQL code on the database to update the table.
            self.cursor.execute("update PipelineConfigurations "
                                "set buildID = '" + str(buildID) + "' ,"
                                "pipelineID = '" + str(pipelineID) + "' ,"
                                "agentID = '" + str(agentID) + "' ,"
                                "driveType = '" + str(driveType) + "' ,"
                                "environment = '" + str(environment) + "' ,"
                                "globalFlag = '" + str(globalFlag) + "' "
                                "where configID = '" + str(configID) + "';")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def pipeline_configs_insert(self, configID, buildID, pipelineID, agentID, driveType, environment, globalFlag):
        """Inserts a value to the PipelineConfigurations table."""
        try:
            takenNames = self.pipeline_configs_get_names()
            if (configID in takenNames):
                return False
            #Converts globalFlag to a string if it's being represented by 0 or 1
            if type(globalFlag) == 'int' or type(globalFlag) == 'bool':
                if globalFlag == 1 or globalFlag == True:
                    globalFlag = 'True'
                if globalFlag == 0 or globalFlag == False:
                    globalFlag = 'False'
            #Calls SQL code on the database to insert into the table.
            self.cursor.execute("insert into PipelineConfigurations (configID, buildID, pipelineID, agentID, driveType, environment, globalFlag) values "
                                "('" + str(configID) + "', '" + str(buildID) + "', '" + str(pipelineID) + "', '" + str(agentID) + "', '" +
                                str(driveType) + "', '" + str(environment) + "', '" + str(globalFlag) + "');")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def pipeline_configs_delete(self, configID):
        """Deletes a value from the PipelineConfigurations table."""
        try:
            #First deletes from tables that require foreign key to the configID.
            self.cursor.execute("delete from access "
                                "where configID = '" + str(configID) + "';")
            self.cursor.execute("delete from artifacts "
                                "where configID = '" + str(configID) + "';")
            self.cursor.execute("delete from tags "
                                "where configID = '" + str(configID) + "';")
            # Commits to update the table
            self.cnxn.commit()
            #Lastly deletes from the pipelineConfigurations table.
            self.cursor.execute("delete from pipelineConfigurations "
                                "where configID = '" + str(configID) + "';")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def pipeline_configs_get_names(self):
        """Retrieves all pipeline configuration names."""
        #Calls SQL code on the database to retrieve all configID names.
        self.cursor.execute("select configID from PipelineConfigurations;")
        #Creates and returns a list of all the names.
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def pipeline_configs_get(self, configID):
        """Retrieves all information of a specific configuration."""
        #Calls SQL code on the database to retrieve all information about a configuration.
        self.cursor.execute("select * from PipelineConfigurations "
                            "where configID = '" + str(configID) + "';")
        #Creates a dictionary of all the information of the configuration.
        row = self.cursor.fetchone()
        configuration = {'configID' : str(row[0]),
                         'buildID' : str(row[1]),
                         'pipelineID' : str(row[2]),
                         'agentID' : str(row[3]),
                         'driveType' : str(row[4]),
                         'environment' : str(row[5]),
                         'globalFlag' : str(row[6])}
        return configuration

    def access_delete(self, configID, userName):
        """Deletes a value from the Access table."""
        try:
            #Calls SQL code on the database to delete an entry from the Access table.
            self.cursor.execute("delete from Access "
                                "where configID = '" + str(configID) + "' AND userName = '" + str(userName) +"';")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def access_insert(self, configID, userName):
        """Inserts a value into the Access table."""
        try:
            values = self.__access_get_by_username(userName)
            if (configID in values):
                return False
            #Calls SQL code on the database to insert an entry into the Access table.
            self.cursor.execute("insert into Access (configID, userName) values ('" + str(configID) + "', '" + str(userName) + "');")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def __access_get_by_username(self, userName):
        """Gets the configurations that a user has been given explicit access to."""
        self.cursor.execute("select configID from access "
                            "where userName = '" + str(userName) + "';")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def access_get(self, userName):
        """Gets the configurations available to a given user."""
        #Calls SQL code on the database to retrieve all configuration the user has access to, whether the configuration is public
        #or the user has private access
        self.cursor.execute("select p.configId from PipelineConfigurations p "
                            "left join Access a "
                            "on p.configID = a.configID "
                            "where a.userName = '" + str(userName) + "' OR p.globalFlag = 1;")
        #Creates and returns a list of configuration names
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def artifacts_delete(self, configID, artifactID):
        """Deletes a value from the Artifacts table."""
        try:
            #Calls SQL code on the database to delete an entry from the Artifacts table.
            self.cursor.execute("delete from Artifacts "
                                "where configID = '" + str(configID) + "' AND artifactID = '" + str(artifactID) + "';")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def artifacts_insert(self, configID, artifactID):
        """Inserts a value into the Artifacts table."""
        try:
            artifacts = self.artifacts_get(configID)
            if (artifactID in artifacts):
                return False
            #Calls SQL code on the database to insert an entry into the Artifacts table.
            self.cursor.execute("insert into Artifacts (configID, artifactID) values ('" + str(configID) + "', '" + str(artifactID) + "');")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def artifacts_get(self, configID):
        """Gets the artifacts for a given configuration."""\
        #Calls SQL code on the database to select all artifact names associated with a configuration ID.
        self.cursor.execute("select artifactID from Artifacts "
                            "where configID = '" + str(configID) + "';")
        #Creates and returns a list of artifact names
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def tags_insert(self, configID, tagName):
        """Inserts a value into the Tags table."""
        try:
            tagNames = self.tags_get(configID)
            if (tagName in tagNames):
                return False
            #Calls SQL code on the database to insert an entry into the tags table.
            self.cursor.execute("insert into tags (configID, tagName) values ('" + str(configID) + "', '" + str(tagName) + "');")
            # Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def tags_delete(self, configID, tagName):
        """Deletes a value from the Tags table."""
        try:
            #Calls SQL code on the database to delete an entry from the tags table.
            self.cursor.execute("delete from tags "
                                "where configID = '" + str(configID) + "' AND tagName = '" + str(tagName) + "';")
            #Commits to update the table
            self.cnxn.commit()
            return True
        except:
            return False

    def tags_get(self, configID):
        """Gets the tags for a given configuration."""
        #Calls SQL code on the database to select all tags associated with a configuration ID.
        self.cursor.execute("Select tagName from Tags "
                            "where configID = '" + str(configID) + "';")
        #Creates and returns a list of tags
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def drive_types_get(self):
        """Gets a list of drive types from the DriveTypes table."""
        #Calls SQL code on the database to select all drive types
        self.cursor.execute("select * from drivetypes;")
        #Creates and returns a list of drive types
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def environment_get(self):
        """Gets a list of environments from the Environments table."""
        #Calls SQL code on the database to select all environments
        self.cursor.execute("Select * from environments;")
        #Creates and returns a list of environments
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def buildIDs_get(self, driveType, testEnv):
        """Gets a buildID given the drive type and the test environment."""
        self.cursor.execute("Select buildID from buildIDs "
                            "where driveType = '" + str(driveType) + "' and testEnvironment = '" + str(testEnv) + "';")
        row = self.cursor.fetchone()
        if row:
            value = str(row[0])
            return value
        return None

    def absoluteIDs_get(self, buildID):
        """Gets the absolute IDs of builds associated with buildID"""
        self.cursor.execute("Select absoluteID from absoluteIDs "
                            "where buildID = '" + str(buildID) + "';")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def buildIDs_getAll(self):
        self.cursor.execute("Select buildID from buildIDs; ")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def buildIDs_insert(self, buildID, driveType, testEnv):
        """Insert a value into the buildIDs table."""
        value = self.buildIDs_get(driveType, testEnv)
        if (value):
            return False
        value = self.buildIDs_getAll()
        if str(buildID) in value:
            return False
        self.cursor.execute("Insert into buildIDs (buildID, driveType, testEnvironment) values ('"
                            + str(buildID) + "', '" + str(driveType) + "', '" + str(testEnv) + "');")
        self.cnxn.commit()
        return True