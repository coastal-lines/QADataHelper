#import re

class UserQueryObject:
    def __init__(self, original_query, where, condition, text):
        self.original_query = original_query
        self.where = where
        self.condition = condition
        self.text = text

class UserQueriesObject:
    def __init__(self):
        self.__userQueriesObjects = []
        
    def add_query(self, userQueryObject):
        self.__userQueriesObjects.append(userQueryObject)

    def get_queries(self):
        return self.__userQueriesObjects
