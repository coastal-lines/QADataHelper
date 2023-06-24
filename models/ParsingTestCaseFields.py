

class ParsingTestCaseFields:

    def __init__(self, server, test_case_fields):
        self.server = server
        self.test_case_fields = test_case_fields

        self.api = RestApi(self.server)

        self.__previous_test_case_folder_name = None
        self.__previous_parents = None
        
    def _set_field_for_test_case(self, current_tc_as_object, number_position, value):
        current_tc_as_object.__setattr__(self.test_case_fields[number_position], value)

    def _get_simple_field_as_string(self, test_case, attr_number):
        return getattr(test_case, self.test_case_fields[attr_number])
        
    def _get_total_duration_for_one_test_case(self, objectID, credits):
        results = self.api.get_total_duration(objectID, credits)

        total_time = 0
        number_results_with_duration = 0
        for result in results:
            if (result["Duration"] != None):
                total_time += result["Duration"]
                number_results_with_duration += 1

        if(total_time != 0):
            total_time = total_time / number_results_with_duration

        return total_time
        
    def _get_project_as_string(self, test_case, attr_number):
        return getattr(test_case, self.test_case_fields[attr_number]).Name
        
    def _get_test_folder_as_string(self, test_case, attr_number):
        if (test_case.TestFolder == None):
           return ""
        else:
            return getattr(test_case, self.test_case_fields[attr_number]).Name
