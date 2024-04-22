## QA Data Helper
##### Data Visualization, Statistics and Metrics for daily testing tasks

#
#

![image](https://github.com/coastal-lines/QADataHelper/blob/master/resources/data/doc/main_scr.jpg?raw=true)

#

#### Features
- Search capabilities
    - Using the original search syntax from Rally Agile
    - Additional search options within Input and Expected fields

- Displaying the structure of tests
    - View the structure of test cases as a tree instead of non-informative sheet
    - Simple way to copy filtered test list into feature, test report, etc

- Data visualization
    - Ratio of successful test cases to unsuccessful ones
    - Number of defects for each Priority
    - Ratio of manual test case execution time to automated
    - Number of test steps and average number of text lines in steps
    - Ratio of manual to automated test cases
    - Display of the number of test cases for each type

- Defect chart for a set of test cases
    - For the entire period from the earliest defect to the latest
    - For a three-month period (depending on the project’s release frequency)

- Advanced search and visualization of statistics for selective parameters
    - Ratio of selective test cases to the total number of cases
    - Output of brief statistics for each selective set

#

#### Used python version
- 3.12.2

#

#### Installation (cmd)
- Please check your python version 
```sh
python --version
```
- Clone this project into your machine
```sh
cd <your_projects_folder>
git clone https://github.com/coastal-lines/QADataHelper.git
cd QADataHelper
```
- Create virtual environment and activate it
```sh
python -m venv venv
venv\Scripts\activate
```
- Install requirements
```sh
pip install -r requirements.txt
```
- Please check that [Tkinter](https://tkdocs.com/tutorial/install.html#installwin) library is included in the default python installation
```sh
python
>>> import tkinter
>>> tkinter._test()
```

#
