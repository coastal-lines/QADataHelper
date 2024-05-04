from models.model import Model
from utils import file_helper
from views.view import View
from service_components.service_folder import ServiceFolder
from service_components.service_instance import ServiceInstance


class Controller():
    def __init__(self, view_mode: str = None):
        self.view = View(self, view_mode)
        self.model = Model(self.view.get_server_instance())

        self.service = None
        self.root_folder = None
        self.test_cases = None

    def main(self):
        self.view.main()

    def on_start_session_click(self, server: str, user: str, password: str, workspace: str, project: str, root_folder: str):
        try:
            self.service = ServiceInstance(server, user, password)
            self.service.set_workspace(workspace)
            self.service.set_project(project)

            if(root_folder != ""):
                self.root_folder = ServiceFolder(self.service, root_folder)
                self.root_folder_formatted_id = self.root_folder.get_test_folder()

            print("Session starts")

            self.view.lock_save_test_cases_button()
        except:
            print("Communication error")
            
    def on_download_all_test_cases_click(self, credits, rootForTestCases, rootForFolders):
        test_cases = self.model.download_all_test_cases(self.root_folder,
                                                        self.service,
                                                        credits,
                                                        rootForTestCases,
                                                        rootForFolders)

        file_helper.save_test_cases_into_file(test_cases)

    def on_upload_all_test_cases_click(self):
        self.test_cases = self.model.upload_all_test_cases(file_helper.call_file_open_dialog())
        self.view.set_upload_mode()
        self.view.update_view(self.test_cases)
        self.view.switch_active_tab(1)
        
    def on_find_test_cases_click(self, user_query_text):
        self.model.clear_list_test_cases()
        self.view.unlock_save_test_cases_button()
        self.test_cases = self.model.run_query(self.service,
                                               self.view.setup_tab.get_credits(),
                                               user_query_text,
                                               self.view.setup_tab.get_project_for_test_cases(),
                                               self.view.setup_tab.get_project_for_folders())
        self.view.unlock_save_test_cases_button()
        self.view.update_view(self.test_cases)
        
    def on_find_extra_test_cases_click(self, user_query_text: str):
        if(user_query_text != ""):
            test_cases, result_for_statistics_tab = self.model.run_extra_query(user_query_text)

            if(len(test_cases) == 0):
                print("Test cases were not found")
                self.view.update_view_null_result()
            else:
                #update test cases list
                self.view.update_view(test_cases)
                self.view.update_view_extended_details(result_for_statistics_tab, len(self.model.get_test_cases()))
                
    def on_save_found_test_cases_click(self):
        file_helper.save_test_cases_into_file(self.test_cases)
