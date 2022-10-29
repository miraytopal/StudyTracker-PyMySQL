from StudyTracker.analysis_interface import *

while True:
    choice = input(
        '''\nPlease enter your transaction what you want do:
             1. Add category
             2. Add study record
             3. Show all record history of study
             4. Analyze your study records
             5. Delete category
             6. Exit
        ''')

    if choice == '1':
        category_name = input('Please enter category name: ')
        db_con.insert_into_category(category_name)

    elif choice == '2':
        db_con.show_category_info()
        category_id = int(input('Please enter category id: '))
        study_time = int(input('Please enter your study time in minutes: '))
        date = ('Please enter date(The system can take date as default): ')
        db_con.insert_into_study(category_id, study_time)

    elif choice == '3':
        db_con.show_study_history()

    elif choice == '4':
        user_analysis_interface()

    elif choice == '5':
        db_con.show_category_info()
        category_id = int(input('Please enter category id you want to delete: '))
        db_con.delete_category(category_id)

    elif choice == '6':
        db_con.close_connection()
        break

    else:
        print('Please enter a valid number')