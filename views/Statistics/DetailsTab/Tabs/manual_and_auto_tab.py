import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from utils.visualization_helper import VisualizationHelper

class ManualAutoTab(VisualizationHelper):

    def update_manual_auto(self, details_frame, test_cases):
        plt.rcParams['font.size'] = 10

        manual = 0
        auto= 0
        for tc in test_cases:
            if(tc.Method == "Manual"):
                manual += 1
            else:
                auto += 1

        testing_method_fig, testing_method_ax = plt.subplots()
        testing_method_ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        testing_method_ax.bar(['Manual'], [manual], color="cornflowerblue")
        testing_method_ax.bar(['Auto'], [auto], color="lightsteelblue")
        testing_method_ax.set_title('Manual/Auto')

        self.create_canvas(details_frame, testing_method_fig, 400, 300)