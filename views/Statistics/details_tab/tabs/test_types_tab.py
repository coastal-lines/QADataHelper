from typing import List

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from service_components.service_test_case import ServiceTestCase
from utils import visualization_helper
from utils.config_reader import ConfigReader


class TestTypesTab():

    def update_test_types(self, details_frame, test_cases: List[ServiceTestCase]):
        test_types = ConfigReader().get_parameters("TESTTYPES")

        test_types_dict = dict()
        for i in range(len(test_types)):
            test_types_dict[test_types[i]] = 0

            for tc in test_cases:
                if (tc.Type == test_types[i]):
                    test_types_dict[test_types[i]] = test_types_dict[test_types[i]] + 1

        test_type_fig, test_type_ax = plt.subplots()
        test_type_fig.suptitle('Test types', fontsize=12)
        test_type_fig.subplots_adjust(left=0.25)

        test_type_ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.yticks(fontsize=8)

        for type in test_types_dict:
            test_type_ax.barh([type], [test_types_dict[type]], color="cornflowerblue", align='center', alpha=0.4)

        visualization_helper.create_canvas(details_frame, test_type_fig, 800, 300)