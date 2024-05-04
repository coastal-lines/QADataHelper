import datetime
import tkinter as tk
from typing import List

import matplotlib.pyplot as plt
import pandas as pd
from dateutil.relativedelta import relativedelta
import seaborn as sns

from service_components.service_test_case import ServiceTestCase
from utils import visualization_helper


class DefectsTimeLine:
    __DEFECTS_LIMIT = 35

    def __init__(self):
        self.defects_time_line_frame = tk.Frame()
        self.defects_time_line_frame.place()

    def update_defects_full_timeline(self, test_cases: List[ServiceTestCase]):
        sorted_defects_by_date = sorted([defect.get_defect() for tc in test_cases for defect in tc.DefectsInformation.get_defects_list()])

        start_date = pd.to_datetime(sorted_defects_by_date[0][0])
        end_date = pd.to_datetime(str(datetime.date.today()))

        sorted_year_month = pd.date_range(start=pd.to_datetime(start_date), end=pd.to_datetime(end_date), freq='M').strftime('%Y-%m').tolist()

        data_frame = {
            'Date': sorted_year_month,
            'P1': [0] * len(sorted_year_month),
            'P2': [0] * len(sorted_year_month),
            'P3': [0] * len(sorted_year_month),
            'P4': [0] * len(sorted_year_month),
            'P5': [0] * len(sorted_year_month)
        }

        for i in range(len(sorted_year_month)):
            for defect_date in sorted_defects_by_date:
                if(sorted_year_month[i] == pd.to_datetime(defect_date[0]).strftime('%Y-%m')):
                    data_frame[defect_date[1]][i] += 1

        #remove all columns with date if column doesn't have any defect
        df = pd.DataFrame(data_frame)
        df = df[df.iloc[:, 1:].any(axis=1)]
        df_dict = df.to_dict(orient='list')

        #add the latest column for finish all defects lines
        for key, value in pd.DataFrame(data_frame).iloc[-1,:].to_dict().items():
            df_dict[key].append(value)

        _fig, _ax = plt.subplots()

        sns.lineplot(x="Date", y="P1", data=df_dict, color="orange", label="P1", alpha=0.7)
        sns.lineplot(x="Date", y="P2", data=df_dict, color="red", label="P2", alpha=0.7)
        sns.lineplot(x="Date", y="P3", data=df_dict, color="green", label="P3", alpha=0.7)
        sns.lineplot(x="Date", y="P4", data=df_dict, color="blue", label="P4", alpha=0.7)
        sns.lineplot(x="Date", y="P5", data=df_dict, color="purple", label="P5", alpha=0.7)

        plt.title(f"Defects for the period from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")

        plt.xticks(rotation=20)
        plt.ylim(0, self.__DEFECTS_LIMIT)
        plt.xlim(start_date.strftime('%Y-%m'), end_date.strftime('%Y-%m'))
        plt.ylabel("Number defects")

        _fig.autofmt_xdate()

        visualization_helper.create_full_tab_canvas(self.defects_time_line_frame, _fig, 12.0, 3.5, 0, 0)

    def update_defects_three_months_timeline(self, test_cases: List[ServiceTestCase]):
        sorted_defects_by_date = sorted([defect.get_defect() for tc in test_cases for defect in tc.DefectsInformation.get_defects_list()])

        start_date = pd.to_datetime(str((datetime.date.today() + relativedelta(months=1)) - relativedelta(months=3)))
        end_date = pd.to_datetime(str(datetime.date.today() + relativedelta(months=1)))
        sorted_year_month = pd.date_range(start=start_date, end=end_date, freq='M').strftime('%Y-%m').tolist()

        data_frame = {
            'Date': sorted_year_month,
            'P1': [0] * len(sorted_year_month),
            'P2': [0] * len(sorted_year_month),
            'P3': [0] * len(sorted_year_month),
            'P4': [0] * len(sorted_year_month),
            'P5': [0] * len(sorted_year_month)
        }

        for i in range(len(sorted_year_month)):
            for defect_date in sorted_defects_by_date:
                if(sorted_year_month[i] == pd.to_datetime(defect_date[0]).strftime('%Y-%m')):
                    data_frame[defect_date[1]][i] += 1

        _fig, _ax = plt.subplots()

        #plotting information
        sns.lineplot(x="Date", y="P1", data=data_frame, color="orange", label="P1", alpha=0.7)
        sns.lineplot(x="Date", y="P2", data=data_frame, color="red", label="P2", alpha=0.7)
        sns.lineplot(x="Date", y="P3", data=data_frame, color="green", label="P3", alpha=0.7)
        sns.lineplot(x="Date", y="P4", data=data_frame, color="blue", label="P4", alpha=0.7)
        sns.lineplot(x="Date", y="P5", data=data_frame, color="purple", label="P5", alpha=0.7)

        plt.title("Defects for the last three months:")

        plt.xticks(rotation=20)
        plt.ylim(0, self.__DEFECTS_LIMIT)
        plt.xlim(data_frame["Date"][0], data_frame["Date"][-1])

        plt.xlabel("Months")
        plt.ylabel("Number defects")

        _fig.autofmt_xdate()

        visualization_helper.create_full_tab_canvas(self.defects_time_line_frame, _fig, 12.0, 2.7, 0, 353)

