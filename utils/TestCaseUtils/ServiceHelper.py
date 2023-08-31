class ApiServiceHelper:
    def get_folder(self, service, query):
        return service.get('TestFolder', fetch=True, projectScopeDown=True, query=query)

