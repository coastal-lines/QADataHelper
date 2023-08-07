from models.CalculationStatisticsForTestCaseFields import CalculationStatisticsForTestCaseFields

class _UserQueryData:
    def __init__(self):
        self.query = None
        self.number_tc = None
        self.number_other_tc = None
        self.number_defects = None
        self.number_auto = None
        self.number_manual = None
        self.duration = None
        self.number_steps = None
        self.average_number_lines_of_steps = None

class DataFormatter:
    def prepare_user_queries_for_statistics(self, combined_queries, number_all_test_cases):
        prepared_data = []

        for queries in combined_queries:
            for data in queries[1].get_queries():
                temp = _UserQueryData()
                temp.query = data.original_query
                temp.number_tc = len(queries[0])
                temp.number_other_tc = str(int(number_all_test_cases) - len(queries[0]))
                temp.duration = CalculationStatisticsForTestCaseFields().get_average_duration_for_test_cases(queries[0])
                temp.number_manual, temp.number_auto = CalculationStatisticsForTestCaseFields().get_number_manual_and_auto_for_test_cases(queries[0])
                temp.number_defects = CalculationStatisticsForTestCaseFields().get_number_defects_for_test_cases(queries[0])
                temp.number_steps, temp.average_number_lines_of_steps = CalculationStatisticsForTestCaseFields().get_average_of_steps_lines_for_test_cases(queries[0])

            prepared_data.append(temp)

        return prepared_data