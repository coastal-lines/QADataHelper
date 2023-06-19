

class ParsingTestCaseFields:

    def __init__(self, server, test_case_fields):
        self.server = server
        self.test_case_fields = test_case_fields

        self.api = RestApi(self.server)

        self.__previous_test_case_folder_name = None
        self.__previous_parents = None
        
    def _set_field_for_test_case(self, current_tc_as_object, number_position, value):
        current_tc_as_object.__setattr__(self.test_case_fields[number_position], value)

