import re
from typing import Tuple, List

from models.queries.user_queries_object import UserQueriesObject
from models.queries.user_query_object import UserQueryObject
from service_components.service_test_case import ServiceTestCase


class QueryFormatter:
    def __try_regexp(self, raw_query: str) -> List[str]:

        # split raw query by brackets
        pattern = r"\((.*?)\)"
        result = re.findall(pattern, raw_query)

        return result

    def __split_raw_query_into_combined_queries(self, raw_query: str) -> List[str]:
        combined_queries = self.__try_regexp(raw_query)

        return combined_queries

    def __remove_extra_bracket(self, phrase: str, word: str) -> Tuple[str, str]:
        word = word.replace("(", "")
        phrase = phrase.replace("(", "")
        return phrase, word

    def __split_each_query(self, raw_query: str) -> Tuple[str,str,str]:
        words = raw_query.split(" ")

        # if query starts from space then remove this
        if (words[0] == " " or words[0] == ""):
            words.pop(0)

        where = words[0]
        condition = words[1]
        text = raw_query[raw_query.find('"') + 1:-1].strip('"')
        print("where: " + where, "condition: " + condition, "text: " + text)

        return where, condition, text

    def __try_to_find_user_query_in_string(self, current_test_case_value, text):
        is_user_query_in_text = False

        if (isinstance(current_test_case_value, str)):
            if (text.lower() in str(current_test_case_value).lower()):
                is_user_query_in_text = True
        else:
            is_user_query_in_text = self.__try_to_find_user_query_in_list(current_test_case_value, text)

        return is_user_query_in_text

    def __try_to_find_user_query_in_list(self, current_test_case_value, text):
        if (current_test_case_value, list):
            full_text = ""
            for item in current_test_case_value:
                full_text = full_text + " " + str(item)

            if (text.lower() in full_text.lower()):
                return True

    def split_raw_query_by_logical_operator(self, raw_query: str) -> List[UserQueriesObject]:
        combined_queries = self.__split_raw_query_into_combined_queries(raw_query)

        user_queries = []
        for combined_query in combined_queries:
            user_queries.append(UserQueriesObject())

            if ("OR" in combined_query):
                list_queries = combined_query.split("OR")

                for query in list_queries:
                    w, c, t = self.__split_each_query(query)
                    if (w[0] == "("):
                        combined_query, w = self.__remove_extra_bracket(combined_query, w)

                    user_query = UserQueryObject(query, w, c, t)
                    user_queries[-1].add_query(user_query)
            else:
                w, c, t = self.__split_each_query(combined_query)
                if (w[0] == "("):
                    combined_query, w = self.__remove_extra_bracket(combined_query, w)

                user_query = UserQueryObject(combined_query, w, c, t)
                user_queries[-1].add_query(user_query)

        return user_queries

    def select_test_cases_by_query(self, list_test_cases: List[ServiceTestCase], test_case_fields: List[str], where: str, text: str) -> List[ServiceTestCase]:
        result = []

        for test_case in list_test_cases:
            for field in test_case_fields:
                if (where.lower() == field.lower()):

                    current_test_case_value = test_case.__getattribute__(where)

                    if (self.__try_to_find_user_query_in_string(current_test_case_value, text)):
                        result.append(test_case)
                        continue

        return result


