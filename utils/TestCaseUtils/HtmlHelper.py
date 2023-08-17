from bs4 import BeautifulSoup
import re

class HtmlHelper:

    def __is_text_in_string(self, text, string):
        result = False

        pattern = re.compile(r"'(\w+) :")
        match = pattern.findall(string)

        for m in match:
            if(text in m):
                result = True

        return result

    #update_tree_tab_view step 1
    def formTree(self, test_cases):
        tree = dict()

        list_test_cases = []
        list_test_cases_without_parents = []
        for tc in test_cases:
            if(tc.Parents != ""):
                list_test_cases.append(tc.Parents)
            else:
                list_test_cases_without_parents.append(tc)

        for item in list_test_cases:
            currentTree = tree
            self.__temp = []
            for key in item:
                if(self.__is_text_in_string(str(key), str(currentTree)) == False):
                    value = key + " : " + item[key]
                    currentTree[value] = dict()
                else:
                    value = key + " : " + item[key]

                currentTree = currentTree[value]

        return tree, list_test_cases_without_parents
