from utils.TestCaseUtils.HtmlHelper import HtmlHelper
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

 