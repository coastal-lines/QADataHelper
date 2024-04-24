import os
from dataclasses import dataclass

from utils import file_helper


@dataclass
class Resources:
    structure_testcases_html_file = os.path.join(file_helper.get_project_resources_directory(), "structure_testcases_html.html")
    no_results_testcases_html_file = os.path.join(file_helper.get_project_resources_directory(), "null_results_html.html")