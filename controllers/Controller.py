from models.Model import Model
from views.View import View
from service_components.ServiceFolder import ServiceFolder
from service_components.ServiceInstance import ServiceInstance
from utils.FileHelper import FileHelper

class Controller():

    def __init__(self):
        self.view = View(self)
        self.model = Model(self.view.get_server_instance())
        self.rootFolder = None
        self.test_cases = None

        self.file_helper = FileHelper()

    def main(self):
        self.view.main()

    def on_start_session_click(self, server, user, password, workspace, project, root_folder):
        try:
            self.service = ServiceInstance(server, user, password).service
            self.service.setWorkspace(workspace)
            self.service.setProject(project)

            if(root_folder != ""):
                self.rootFolder = ServiceFolder(self.service, 'FormattedID = "' + root_folder + '"').testFolder
                self.root_folder_formatted_id = root_folder

            print("Session starts")

            self.view.lock_save_test_cases_button()
        except:
            print("Communication error")
            
    def on_download_all_test_cases_click(self, credits, rootForTestCases, rootForFolders):
        test_cases = self.model.download_all_test_cases(self.rootFolder,
                                                        self.service,
                                                        credits,
                                                        rootForTestCases,
                                                        rootForFolders)

        self.file_helper.save_test_cases_into_file(test_cases)
       

