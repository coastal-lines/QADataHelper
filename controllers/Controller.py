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

