from bs4 import BeautifulSoup
import re

from resources.resources_dataclass import Resources
from utils import file_helper


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
        
    # update_tree_tab_view step 2
    def traversal_tree(self, tree, html_document, list_test_cases_without_parents):
        root = html_document.find_all("ul")[-1]

        for k in tree:
            if (len(html_document.find_all("li", string=k)) == 0):
                new_li = html_document.new_tag("li")
                new_li['style'] = "font-size: 10px;"
                if(k.startswith('TC')):
                    new_li.string = k.replace(":", "")
                else:
                    new_li.string = k
                new_ul = html_document.new_tag("ul")
                root.append(new_li)
                root.append(new_ul)
            else:
                new_li = html_document.new_tag("li")
                new_li['style'] = "font-size: 10px;"
                if (k.startswith('TC')):
                    new_li.string = k.replace(":", "")
                else:
                    new_li.string = k
                new_ul = html_document.new_tag("ul")

                last_ul = html_document.find_all("ul")[-1]
                last_ul.append(new_li)
                last_ul.append(new_ul)

            if (len(tree[k]) > 0):
                self.traversal_tree(tree[k], html_document, list_test_cases_without_parents)
            else:
                new_ul = html_document.new_tag("ul")
                last_ul = html_document.find_all("ul")[-1]
                last_ul.append(new_ul)

    #some of test cases can be without parents
    def add_unstructured_test_cases_into_html(self, html_document, list_test_cases_without_parents):
        unstructured_h3 = html_document.new_tag("h3")
        new_ul = html_document.new_tag("ul")

        for tc in list_test_cases_without_parents:
            new_li = html_document.new_tag("li")
            new_li['style'] = "font-size: 10px;"
            new_li.string = tc.FormattedID + ": " + tc.Name
            new_ul.append(new_li)

        root = html_document.find("body")
        unstructured_h3.string = "Unstructured test cases:"
        root.append(unstructured_h3)
        root.append(new_ul)
        
    def create_html(self, list):
        html_base = file_helper.load_file(Resources.structure_testcases_html_file)

        html_document = BeautifulSoup(html_base, 'html.parser')
        tree, list_test_cases_without_parents = self.formTree(list)
        self.traversal_tree(tree, html_document, list_test_cases_without_parents)

        if (len(list_test_cases_without_parents) > 0):
            self.add_unstructured_test_cases_into_html(html_document, list_test_cases_without_parents)

        return html_document
        
    #for tc steps
    def get_str_list_from_html(self, raw_html_array):

        html_base = ""
        html_document = BeautifulSoup(html_base, 'html.parser')
        for line in raw_html_array:
            html_document.append(line)
        prt = html_document.prettify()
        str_list = list(filter(None, prt.split("\n")))

        return str_list