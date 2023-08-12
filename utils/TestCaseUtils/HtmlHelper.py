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


