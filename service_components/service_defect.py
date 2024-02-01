class ServiceDefect:
    def __init__(self, data, severity):
        self.__defect = (data, severity)

    def get_defect(self):
        return self.__defect