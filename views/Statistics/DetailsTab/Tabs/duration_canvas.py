import matplotlib.pyplot as plt

from models.CalculationStatisticsForTestCaseFields import CalculationStatisticsForTestCaseFields
from utils.VisualizationHelper import Visualization

class DurationCanvas(Visualization):

    def update_duration(self, details_frame, test_cases):
        manual_time_duration, auto_time_duration = CalculationStatisticsForTestCaseFields().get_average_duration_for_test_cases(test_cases)

        duration_fig3, duration_ax3 = plt.subplots()
        duration_ax3.set_title('Duration')
        duration_ax3.set_xlabel(f'\n\n\n Total test cases duration - {manual_time_duration + auto_time_duration} minutes', fontsize=8)

        duration_fig3.set_size_inches(4.0, 3.0)
        duration_ax3.bar(['Manual duration'], [manual_time_duration], color="cornflowerblue")
        duration_ax3.bar(['Auto duration'], [auto_time_duration], color="lightsteelblue")

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        duration_fig3.subplots_adjust(bottom=0.3)

        self.create_canvas(details_frame, duration_fig3, 800, 0)