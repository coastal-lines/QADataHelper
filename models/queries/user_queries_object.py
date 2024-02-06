class UserQueriesObject:
    def __init__(self):
        self.__userQueriesObjects = []

    def add_query(self, userQueryObject):
        self.__userQueriesObjects.append(userQueryObject)

    def get_queries(self):
        return self.__userQueriesObjects