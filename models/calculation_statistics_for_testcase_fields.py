from utils.TestCaseUtils.html_helper import HtmlHelper
import operator


class CalculationStatisticsForTestCaseFields:
    def get_number_manual_and_auto_for_test_cases(self, test_cases):
        manual = 0
        auto= 0

        for tc in test_cases:
            if(tc.Method == "Manual"):
                manual += 1
            else:
                auto += 1

        return manual, auto

    def get_average_of_steps_lines_for_test_cases(self, test_cases):
        inputs = []
        expecteds = []
        number_steps = []

        for tc in test_cases:
            for input in tc.Inputs:
                inputs.append(input)
                number_steps.append(input)

            for expected in tc.Expecteds:
                expecteds.append(expected)

        input_list = HtmlHelper().get_str_list_from_html(inputs)
        expected_list = HtmlHelper().get_str_list_from_html(expecteds)
        average_number_lines_of_steps = (len(input_list) + len(expected_list)) // 2

        return len(number_steps), average_number_lines_of_steps

    def get_average_duration_for_test_cases(self, test_cases):
        manual_time_duration = 0
        auto_time_duration = 0

        for tc in test_cases:
            if (tc.TotalDuration != 0):
                if(tc.Method == "Manual"):
                    manual_time_duration += tc.TotalDuration
                else:
                    auto_time_duration += tc.TotalDuration

        return manual_time_duration, auto_time_duration
        
    def get_number_defects_for_test_cases(self, test_cases):
        number_defects = 0
        for tc in test_cases:
            number_defects += tc.DefectsInformation.get_total_number_defect()

        return number_defects
        
    def get_number_severities_for_defects(self, test_cases):
        severities = (0,0,0,0,0)

        for tc in test_cases:
            severities_temp = tc.DefectsInformation.get_severities()
            tuple(map(sum, zip(severities, severities_temp)))
            severities = tuple(map(operator.add, severities, severities_temp))

        return severities


