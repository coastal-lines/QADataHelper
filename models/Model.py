

class Model:
    def __init__(self, server):
        self.server = server
        self.list_test_cases = []

        #self.test_case_fields = ConfigReader().get_test_case_fields_from_config()
        self.test_case_fields = None
        self.file_helper = FileHelper()
        self.tc_helper = ParsingTestCaseFields(self.server, self.test_case_fields)

        self.query_formater = QueryFormatter()

    def clear_list_test_cases(self):
        self.list_test_cases.clear()
