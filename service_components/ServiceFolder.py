from utils.TestCaseUtils.ServiceHelper import ApiServiceHelper

class ServiceFolder():
    def __init__(self, service, query):
        testFolderRequest = ApiServiceHelper().get_folder(service, query)
        testFolder = testFolderRequest.next()
        self.testFolder = testFolder