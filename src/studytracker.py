import pandas as pd
from StudyTracker.connect import mysql_connection

class StudyTracker:

    # connection establish
    def __init__(self):
        self.cursor = mysql_connection()

    def table_creator(self):
        try:
            category_table = self.cursor.execute(
                '''CREATE TABLE if not exists categories(
                          category_id INT AUTO_INCREMENT NOT NULL,
                          category_name VARCHAR(100) NOT NULL,
                          PRIMARY KEY (category_id))'''
            )
            study_table = self.cursor.execute(
                '''CREATE TABLE if not exists studies(
                          category_id INT NOT NULL,
                          study_time INT NOT NULL,
                          date date DEFAULT (CURDATE()),
                          FOREIGN KEY (category_id) REFERENCES categories(category_id))'''
            )
            print('Tables created...')

        except Exception as e:
            print(f'Tables couldn\'t created.{e}')

    def insert_into_category(self, category_name):
        category_insert_sql = 'INSERT INTO categories(category_name) VALUES(%s);'
        category_info = self.show_category_info()

        if category_name in [c[1] for c in category_info]:
            print('The category already exists')
        else:
            self.cursor.execute(category_insert_sql, category_name)
            print(f'{category_name} category added.')

    def insert_into_study(self, category_id, time):
        category_info = self.show_category_info()
        if category_id not in [c[0] for c in category_info]:
            print('Invalid category id.\n')
        else:
            study_insert_sql = 'INSERT INTO studies(category_id, study_time) VALUES(%s, %s);'
            self.cursor.execute(study_insert_sql, (category_id, time))

    def delete_category(self, category_id):
        confirm = input(
            '''Are you sure you want to delete? 
            When you delete a category, you will lose all your records linked to the category. 
            Please enter 1 if you are confirming the transaction. 
            Enter any number to exit : '''
        )
        study_delete_sql = ('DELETE FROM studies WHERE category_id = %s;')
        category_delete_sql = ('DELETE FROM categories WHERE category_id = %s;')

        if confirm == '1':
            execute1 = self.cursor.execute(study_delete_sql, category_id)
            execute2 = self.cursor.execute(category_delete_sql, category_id)
            if execute2:
                print('Category deleted...')
            else:
                print('The category could not find...')
        else:
            print('Nothing has been deleted.')

    # to view the information of all categories
    def show_category_info(self):
        self.cursor.execute('SELECT category_id, category_name FROM categories')
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=['CategoryID', 'CategoryName'])
        print(df)
        return rows

    def show_study_history(self):
        self.cursor.execute(
            '''SELECT c.category_id, 
                      c.category_name, 
                      s.study_time, 
                      s.date 
               FROM categories as c
               JOIN studies as s
               ON c.category_id = s.category_id;'''
        )
        history = self.cursor.fetchall()
        df = pd.DataFrame(history, columns=['CategoryID', 'CategoryName', 'StudyTime', 'Date'])
        print(df)

    def close_connection(self):
        self.cursor.close()
        print("Connection closed!")