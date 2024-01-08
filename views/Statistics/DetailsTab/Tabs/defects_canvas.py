import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from models.CalculationStatisticsForTestCaseFields import CalculationStatisticsForTestCaseFields
from utils.visualization_helper import VisualizationHelper


class DefectsCanvas(VisualizationHelper):
    def update_defects(self, details_frame, test_cases):
        number_defects = CalculationStatisticsForTestCaseFields().get_number_defects_for_test_cases(test_cases)

        severities = CalculationStatisticsForTestCaseFields().get_number_severities_for_defects(test_cases)

        defects_fig, defects_ax = plt.subplots()

        defects_ax.set_title(f'Defects')
        defects_ax.set_xlabel(f'\n\n\n Total number of defects - {number_defects}', fontsize=8)

        defects_ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        defects_ax.bar(['P1'], [severities[0]], color="cornflowerblue")
        defects_ax.bar(['P2'], [severities[1]], color="cornflowerblue")
        defects_ax.bar(['P3'], [severities[2]], color="cornflowerblue")
        defects_ax.bar(['P4'], [severities[3]], color="cornflowerblue")
        defects_ax.bar(['P5'], [severities[4]], color="cornflowerblue")

        defects_fig.subplots_adjust(bottom=0.3)

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        if (number_defects == 0):
            defects_fig.text(0.5, 0.5, "No defects", ha="center", va="center", color="black", fontsize=32)

        self.create_canvas(details_frame, defects_fig, 400, 0)