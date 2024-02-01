from service_components.service_defect import ServiceDefect


class ServiceDefects:
    '''
    __total_number: int
    __total_number_severity_p1: int
    __total_number_severity_p2: int
    __total_number_severity_p3: int
    __total_number_severity_p4: int
    __total_number_severity_p5: int
    __created_at: int
    __defects_list: list
    '''

    def __init__(self):
        self.total_number = 0
        self.__total_number_severity_p1 = 0
        self.__total_number_severity_p2 = 0
        self.__total_number_severity_p3 = 0
        self.__total_number_severity_p4 = 0
        self.__total_number_severity_p5 = 0
        self.__created_at = 0
        self.__defects_list = []

    def add_defects(self, defects):
        for defect in defects:
            self.__defects_list.append(
                ServiceDefect(defect["CreationDate"].split("T")[0],
                              defect["Severity"].split(" - ")[0]))

    def set_defects_list(self, defects_list):
        self.__defects_list = defects_list

    def get_defects_list(self):
        return self.__defects_list

    def set_total_number_defect(self, raw_json_defects):
        self.total_number = int(raw_json_defects["TotalResultCount"])

    def get_total_number_defect(self):
        return self.total_number

    def set_severities(self, raw_json_defects):
        for defect in raw_json_defects['Results']:
            severity = defect['Severity'].replace(" ", "").split("-")[0]

            match severity:
                case "P1":
                    self.__total_number_severity_p1 += 1
                    continue
                case "P2":
                    self.__total_number_severity_p2 += 1
                    continue
                case "P3":
                    self.__total_number_severity_p3 += 1
                    continue
                case "P4":
                    self.__total_number_severity_p4 += 1
                    continue
                case "P5":
                    self.__total_number_severity_p5 += 1
                    continue

    def set_severities_manually(self, p1: int, p2: int, p3: int, p4: int, p5: int):
        self.__total_number_severity_p1 = p1
        self.__total_number_severity_p2 = p2
        self.__total_number_severity_p3 = p3
        self.__total_number_severity_p4 = p4
        self.__total_number_severity_p5 = p5

    def get_severities(self):
        return (self.__total_number_severity_p1,
                self.__total_number_severity_p2,
                self.__total_number_severity_p3,
                self.__total_number_severity_p4,
                self.__total_number_severity_p5)