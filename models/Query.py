import re

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
        
class QueryFormatter:
    def try_regexp(self, raw_query):

        #split raw query by brackets
        pattern = r"\((.*?)\)"
        result = re.findall(pattern, raw_query)

        return result
