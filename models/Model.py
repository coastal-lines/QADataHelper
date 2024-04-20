from models.Query import QueryFormatter, UserQueryObject
from models.ParsingTestCaseFields import ParsingTestCaseFields
from service_components.ServiceTestCase import ServiceTestCase
from utils.ConfigReader import ConfigReader
from utils.FileHelper import FileHelper
from utils.TestCaseUtils.ServiceHelper import ApiServiceHelper
from time import sleep

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
        
    def run_query(self, service, rootFolder, credits, user_query_text, rootForTestCases, rootForFolders):
        # get response with User's query
        testCasesFromUserQuery = ApiServiceHelper().get_test_case(service, user_query_text)

        for number in range(testCasesFromUserQuery.resultCount):
            tc = testCasesFromUserQuery.next()
            tcObject = self._init_test_case_as_object(tc, service, credits, rootForTestCases, rootForFolders)
            self.list_test_cases.append(tcObject)

            #TODO - debug
            print(len(self.list_test_cases))
            if((len(self.list_test_cases) / 500).is_integer()):
                print("sleep")
                sleep(91)

        return self.list_test_cases
        
    def upload_all_test_cases(self, file_path):
        self.list_test_cases = self.file_helper.load_files(file_path)
        return self.list_test_cases
        
    #AREA OF HELPFUL METHODS
    def _init_test_case_as_object(self, test_case, service, credits, rootForTestCases, rootForFolders):
        current_tc = ServiceTestCase()

        for attr_number in range(len(self.test_case_fields)):
            self.tc_helper.apply_custom_field_for_test_case(service, current_tc, test_case, attr_number, credits, rootForTestCases, rootForFolders)

            #if field equesl None set empty string
            if(current_tc.__getattribute__(self.test_case_fields[attr_number]) == None):
                current_tc.__setattr__(self.test_case_fields[attr_number], "")

        print(current_tc.Name)

        return current_tc

    #REGION: donload all tc from folder
    
    def download_all_test_cases(self, root_folder, service, credits, rootForTestCases, rootForFolders):
        self.list_test_cases.clear()

        if (len(root_folder.TestCases) > 0 or len(root_folder.Children)):
            self._extract_test_cases_from_folder(root_folder, credits, service, rootForTestCases, rootForFolders)

        print("Size: " + str(len(self.list_test_cases)))

        return self.list_test_cases
        
    _folder_list = []
    def _extract_test_cases_from_folder(self, folder, credits, service, rootForTestCases, rootForFolders):
        self._folder_list.append(folder.Name)

        if len(folder.TestCases) > 0:
            for testCase in folder.TestCases:
                tc = self._init_test_case_as_object(testCase, service, credits, rootForTestCases, rootForFolders)
                self.list_test_cases.append(tc)
                #print(tc.__getattribute__("Parents"))

                # TODO - debug
                print(len(self.list_test_cases))
                if ((len(self.list_test_cases) / 500).is_integer()):
                    print("sleep")
                    sleep(91)

        if len(folder.Children) > 0:
            self._extract_folders(folder.Children, credits, service, rootForTestCases, rootForFolders)
            if(len(self._folder_list) > 1):
                self._folder_list.pop(-1)
                
    def _extract_folders(self, folders, credits, service, rootForTestCases, rootForFolders):
        for folder in folders:
            self._extract_test_cases_from_folder(folder, credits, service, rootForTestCases, rootForFolders)

    #END_REGION