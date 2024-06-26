class ApiServiceHelper:
    def get_folder(self, service, query):
        return service.get('TestFolder', fetch=True, projectScopeDown=True, query=query)

    def get_parent_folder(self, service, testFolderFormattedID):
        return service.get('TestFolder', fetch=True, projectScopeDown=True, query='FormattedID = "' + testFolderFormattedID + '"').next().Parent
        
    def get_test_case(self, service, query):
        return service.get('TestCase', fetch=True, projectScopeDown=True, query=query)