from service_components.service_defects import ServiceDefects
from utils.TestCaseUtils.rest_api_helper import RestApiHelper
from utils.TestCaseUtils.api_service_helper import ApiServiceHelper

class ParsingTestCaseFields:

    def __init__(self, server, test_case_fields):
        self.server = server
        self.test_case_fields = test_case_fields

        self.api = RestApiHelper(self.server)

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
        defects.add_defects(raw_defects_json_result["Results"])

        return defects
        
    def _get_list_of_parents(self, service, testFolderFormattedID, parents):
        temp_parents = parents

        folder = ApiServiceHelper().get_parent_folder(service, testFolderFormattedID)
        temp_parents.update({folder.FormattedID: folder.Name})
        if(folder.Parent != None):
            self._get_list_of_parents(service, folder.FormattedID, temp_parents)
        else:
            return temp_parents
            
    parents = None
    def _get_parents_as_string_graph(self, service, test_case, rootForFolders, rootForTestCases):
        # set parents for building tree structure later
        parents = dict()

        if (test_case.TestFolder != None):

            #check if parents are the same like for previous test case
            if(test_case.TestFolder.Name == self.__previous_test_case_folder_name):
                self.__previous_parents.popitem()
                self.__previous_parents.update({test_case.FormattedID: test_case.Name})
                parents = self.__previous_parents
            else:
                parents = dict()
                parents.update({test_case.FormattedID: test_case.Name})
                parents.update({test_case.TestFolder.FormattedID: test_case.TestFolder.Name})

                service.setProject(rootForFolders)

                self._get_list_of_parents(service, test_case.TestFolder.FormattedID, parents)
                reversed_parents = dict()
                for j in range(len(list(parents)) - 1, -1, -1):
                    reversed_parents.update({list(parents)[j]: parents[list(parents)[j]]})

                parents = reversed_parents

                service.setProject(rootForTestCases)

                self.__previous_test_case_folder_name = test_case.TestFolder.Name
                self.__previous_parents = parents

        return parents.copy()
        
    def apply_custom_field_for_test_case(self, service, current_tc_as_object, test_case, attr_number, credits, rootForTestCases, rootForFolders):
        match self.test_case_fields[attr_number]:
            case "Project":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_project_as_string(test_case, attr_number))
            case "TestFolder":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_test_folder_as_string(test_case, attr_number))
            case "WorkProduct":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_work_product_as_string(test_case, attr_number))
            case "Tags":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_tags_as_string_list(test_case))
            case "Inputs":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_inputs_as_string_list(test_case))
            case "Expecteds":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_expecteds_as_string_list(test_case))
            case "DefectsInformation":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_defects(test_case, credits))
            case "TotalDuration":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_total_duration_for_one_test_case(test_case.ObjectID, credits))
            case "Parents":
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_parents_as_string_graph(service, test_case, rootForFolders, rootForTestCases))
            case _:
                self._set_field_for_test_case(current_tc_as_object, attr_number, self._get_simple_field_as_string(test_case, attr_number))
