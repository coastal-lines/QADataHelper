import matplotlib.pyplot as plt

from utils.TestCaseUtils.HtmlHelper import HtmlHelper
from utils.VisualizationHelper import Visualization

class StepsCanvas(Visualization, HtmlHelper):

    def update_steps(self, details_frame, test_cases):
        number_steps = []
        for tc in test_cases:
            for input in tc.Inputs:
                number_steps.append(input)

        inputs = []
        for tc in test_cases:
            for input in tc.Inputs:
                inputs.append(input)

        input_list = self.get_str_list_from_html(inputs)

        expecteds = []
        for tc in test_cases:
            for expected in tc.Expecteds:
                expecteds.append(expected)

        expected_list = self.get_str_list_from_html(expecteds)

        #TODO - debug, remove after release
        #print(expected_list)
        number_lines_of_steps = (len(input_list) + len(expected_list)) // 2

        steps_fig, steps_ax = plt.subplots()
        steps_ax.bar(['Number of steps'], [len(number_steps)], color="cornflowerblue")
        steps_ax.bar(['Average number of lines in steps'], [number_lines_of_steps], color="lightsteelblue")
        steps_ax.set_title('Steps')

        plt.xticks(fontsize=8)
        self.create_canvas(details_frame, steps_fig, 0, 300)