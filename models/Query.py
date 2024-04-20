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
        
    def split_raw_query_into_combined_queries(self, raw_query):
        combined_queries = self.try_regexp(raw_query)

        return combined_queries

    def split_raw_query_by_logical_operator(self, raw_query):
        combined_queries = self.split_raw_query_into_combined_queries(raw_query)

        user_queries = []
        for combined_query in combined_queries:
            user_queries.append(UserQueriesObject())

            if ("OR" in combined_query):
                list_queries = combined_query.split("OR")

                for query in list_queries:
                    w, c, t = self._split_each_query(query)
                    user_query = UserQueryObject(query, w, c, t)
                    user_queries[-1].add_query(user_query)
            else:
                w, c, t = self._split_each_query(combined_query)
                user_query = UserQueryObject(combined_query, w, c, t)
                user_queries[-1].add_query(user_query)

        return user_queries
        
    def _split_each_query(self, raw_query):
        words = raw_query.split(" ")

        #if query starts from space then remove this
        if (words[0] == " " or words[0] == ""):
            words.pop(0)

        where = words[0]
        condition = words[1]
        text = raw_query[raw_query.find('"') + 1:-1].strip('"')
        print("where: " + where, "condition: " + condition, "text: " + text)

        return where, condition, text
        
    def _select_test_cases_by_query(self, list_test_cases, test_case_fields, where, text):
        result = []

        for test_case in list_test_cases:
            for field in test_case_fields:
                if (where.lower() == field.lower()):

                    current_test_case_value = test_case.__getattribute__(where)

                    if(self._try_to_find_user_query_in_string(current_test_case_value, text)):
                        result.append(test_case)
                        continue

        return result
        
    def _try_to_find_user_query_in_string(self, current_test_case_value, text):
        is_user_query_in_text = False

        if (isinstance(current_test_case_value, str)):
            if (text.lower() in str(current_test_case_value).lower()):
                is_user_query_in_text = True
        else:
            is_user_query_in_text = self._try_to_find_user_query_in_list(current_test_case_value, text)

        return is_user_query_in_text
        
    def _try_to_find_user_query_in_list(self, current_test_case_value, text):
        if(current_test_case_value, list):
            full_text = ""
            for item in current_test_case_value:
                full_text = full_text + " " + str(item)

            if (text.lower() in full_text.lower()):
                return True