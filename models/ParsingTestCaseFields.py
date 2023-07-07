from service_components.ServiceDefects import ServiceDefects
from utils.TestCaseUtils.RestHelper import RestApi
from utils.TestCaseUtils.ServiceHelper import ApiServiceHelper

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
            
    def _get_work_product_as_string(self, test_case, attr_number):
        if (test_case.WorkProduct == None):
            return ""
        else:
            return getattr(test_case, self.test_case_fields[attr_number]).FormattedID
            
    def _get_tags_as_string_list(self, test_case):
        tags = []

        list_tags = test_case.Tags
        for tag in list_tags:
            tags.append(tag.Name)

        return tags
        
    def _get_inputs_as_string_list(self, test_case):
        inputs = []

        list_steps = test_case.Steps
        for item in list_steps:
            inputs.append(item.Input)

        return inputs

    def _get_expecteds_as_string_list(self, test_case):
        expecteds = []

        list_steps = test_case.Steps
        for item in list_steps:
            expecteds.append(item.ExpectedResult)

        return expecteds
        
    def _get_defects(self, test_case, credits):
        raw_defects_json_result = self.api.get_defects(test_case.ObjectID, credits)
        defects = ServiceDefects()
        defects.set_total_number_defect(raw_defects_json_result)
        defects.set_severities(raw_defects_json_result)

        return defects
        
    def _get_list_of_parents(self, service, testFolderFormattedID, parents):
        temp_parents = parents

        folder = ApiServiceHelper().get_parent_folder(service, testFolderFormattedID)
        temp_parents.update({folder.FormattedID: folder.Name})
        if(folder.Parent != None):
            self._get_list_of_parents(service, folder.FormattedID, temp_parents)
        else:
            return temp_parents
