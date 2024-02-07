from service_components.service_instance import ServiceInstance
from utils.testcase_utils.api_service_helper import ApiServiceHelper


class ServiceFolder():
    def __init__(self, service: ServiceInstance, query: str):
        self.__test_folder = ApiServiceHelper().get_folder(service, 'FormattedID = "' + query + '"').next()

    def get_test_folder(self):
        return self.__test_folder