

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

    def get_test_cases(self):
        return self.list_test_cases
        
    def run_extra_query(self, query):
        all_test_cases_result = []
        result = None
        result_for_statistics_tab = []

        self.list_combined_queries = self.query_formater.split_raw_query_by_logical_operator(query)
        for queries in self.list_combined_queries:
            temp_result = None
            result = []
            for user_query in queries.get_queries():
                temp_result = self.query_formater._select_test_cases_by_query(self.list_test_cases, self.test_case_fields, user_query.where, user_query.text)
                result = self.extend_test_case_list(temp_result, result)

            result_for_statistics_tab.append((result, queries))
            all_test_cases_result = self.extend_test_case_list(all_test_cases_result, result)

        print("finish: " + str(len(result)))

        return all_test_cases_result, result_for_statistics_tab
        
    def extend_test_case_list(self, parent_list, temp_list):
        for temp_tc in temp_list:
            if(len([tc for tc in parent_list if tc.FormattedID == temp_tc.FormattedID]) == 0):
                parent_list.append(temp_tc)

        return parent_list