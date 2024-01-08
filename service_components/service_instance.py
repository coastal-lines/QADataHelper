from pyral import Rally

class ServiceInstance():
    def __init__(self, server, user, password):
        self.service = Rally(server, user, password)