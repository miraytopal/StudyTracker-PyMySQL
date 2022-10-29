import pandas as pd
from StudyTracker.connect import mysql_connection

class Analysis:

    def __init__(self):
        self.cursor = mysql_connection()

    # Analysis by date
    def analysis_by_date(self, start_date, ending_date):
        analysis_by_date_sql = '''SELECT SUM(study_time) 
                                  FROM studies
                                  WHERE date BETWEEN %s AND %s;'''

        self.cursor.execute(analysis_by_date_sql, (start_date, ending_date))
        time = self.cursor.fetchone()
        print(f'{time[0]} minutes studied between {start_date} and {ending_date}.')

    # Analysis by category
    def analysis_by_category(self, category_id):
        analysis_category_sql = '''SELECT c.category_id, 
                                          c.category_name, 
                                          SUM(s.study_time)
                                  FROM categories as c
                                  JOIN studies as s
                                  ON c.category_id = s.category_id
                                  WHERE s.category_id = %s;'''

        self.cursor.execute(analysis_category_sql, category_id)
        category = self.cursor.fetchall()
        df = pd.DataFrame(category, columns=['CategoryID', 'CategoryName', 'TotalStudyTime'])
        print(df)

    # Analysis by category and date
    def analysis_by_category_date(self, category_id, start_date, ending_date):
        analysis_category_date_sql = '''SELECT c.category_id, 
                                               c.category_name, 
                                               SUM(s.study_time), 
                                               s.date 
                                        FROM categories as c
                                        JOIN studies as s
                                        ON c.category_id = s.category_id
                                        WHERE s.category_id =%s and (date BETWEEN %s AND %s);'''

        self.cursor.execute(analysis_category_date_sql, category_id)
        category_date = self.cursor.fetchall()
        df = pd.DataFrame(category_date, columns=['CategoryID', 'CategoryName', 'TotalStudyTime', 'Date'])
        print(df)

    # Analysis by all categories and all dates
    def analysis_dates_categories(self):
        analysis_all_sql = '''SELECT c.category_id, 
                                     c.category_name, 
                                     SUM(s.study_time), 
                                     s.date 
                              FROM categories as c
                              JOIN studies as s
                              ON c.category_id = s.category_id
                              GROUP BY s.category_id, s.date;'''

        self.cursor.execute(analysis_all_sql)
        all_category_date = self.cursor.fetchall()
        df = pd.DataFrame(all_category_date, columns=['CategoryID', 'CategoryName', 'TotalStudyTime', 'Date'])
        print(df)

    # Analysis by all dates
    def analysis_all_dates(self):
        analysis_all_dates_sql = '''SELECT SUM(s.study_time), 
                                           s.date
                                    FROM studies as s
                                    GROUP BY s.date;'''

        self.cursor.execute(analysis_all_dates_sql)
        all_dates = self.cursor.fetchall()
        df = pd.DataFrame(all_dates, columns=['TotalStudyTime', 'Date'])
        print(df)

    # Analysis by all of categories
    def analysis_all_categories(self):
        analysis_all_categories_sql = '''SELECT c.category_id, 
                                                c.category_name, 
                                                sum(s.study_time)
                                          FROM categories as c
                                          JOIN studies as s
                                          ON c.category_id = s.category_id
                                          GROUP BY s.category_id;'''

        self.cursor.execute(analysis_all_categories_sql)
        all_categories = self.cursor.fetchall()
        df = pd.DataFrame(all_categories, columns=['CategoryID', 'CategoryName', 'TotalStudyTime'])
        print(df)