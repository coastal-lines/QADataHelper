import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from utils.VisualizationHelper import Visualization

class SuccessCanvas(Visualization):
    def update_success(self, details_frame, test_cases):

        number_passed_tc = 0
        number_other_tc = 0

        for tc in test_cases:
            if(tc.LastVerdict == "Pass"):
                number_passed_tc += 1
            else:
                number_other_tc += 1

        success_fig, success_ax = plt.subplots()

        success_ax.set_title('Success')
        success_ax.set_xlabel(f'\n\n\n Total number of test cases - {len(test_cases)}', fontsize=8)

        success_ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        success_ax.bar(['Passed'], [number_passed_tc], color="cornflowerblue")
        success_ax.bar(['Other'], [number_other_tc], color="lightsteelblue")

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        success_fig.subplots_adjust(bottom=0.3)

        self.create_canvas(details_frame, success_fig, 0, 0)