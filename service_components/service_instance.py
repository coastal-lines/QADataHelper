from pyral import Rally


class ServiceInstance:
    def __init__(self, server: str, user: str, password: str):
        self.__service = Rally(server, user, password)

    def get_service(self) -> Rally:
        return self.__service

    def set_workspace(self, workspace: str):
        self.__service.setWorkspace(workspace)

    def set_project(self, project: str):
        self.__service.setProject(project)