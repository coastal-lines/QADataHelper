class ServiceDefects:
    def __init__(self):
        self.total_number = 0
        self.__total_number_severity_p1 = 0
        self.__total_number_severity_p2 = 0
        self.__total_number_severity_p3 = 0
        self.__total_number_severity_p4 = 0
        self.__total_number_severity_p5 = 0

    def set_total_number_defect(self, raw_json_defects):
        self.total_number = int(raw_json_defects["TotalResultCount"])

    def get_total_number_defect(self):
        return self.total_number

