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

