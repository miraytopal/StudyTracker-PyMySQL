from StudyTracker.studytracker import *
from StudyTracker.analysis import *

db_con = StudyTracker()
db_con.table_creator()
analysis = Analysis()

def user_analysis_interface():
    analysis_type = input(
        '''Please enter your transaction what you want do:
            1. By date
            2. By category
            3. By date and category
            4. General analysis '''
    )

    if analysis_type == '1':
        print(
            '''Please enter a start and a ending time for the date range you want to analyze.
            The date has to be year-month-day[YYYY-MM-DD] format.'''
        )
        start_date = input('Please enter a start time: ')
        ending_date = input('Please enter a ending time: ')
        analysis.analysis_by_date(start_date, ending_date)

    elif analysis_type == '2':
        db_con.show_category_info()
        category_id = int(input('Please enter the category id of the category you want to analyze: '))
        analysis.analysis_by_category(category_id)

    elif analysis_type == '3':
        print(
            '''Please choose one of the categories you see below and enter a start and a ending time for the date range you want to analyze.
            The date has to be year-month-day[YYYY-MM-DD] format.'''
        )
        db_con.show_category_info()
        category_id = int(input('Please enter the category id of the category you want to analyze: '))
        start_date = input('Please enter a start date: ')
        ending_date = input('Please enter a ending date: ')
        analysis.analysis_by_date(start_date, ending_date)

    elif analysis_type == '4':
        analysis.analysis_dates_categories()
        analysis.analysis_all_dates()
        analysis.analysis_all_categories()

    else:
        print('Please enter a valid number')

