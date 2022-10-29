import pymysql

def mysql_connection():
    config = {
        'host': '',
        'port': ,
        'user': '',
        'password': '',
        'database': '',
        'autocommit': True
    }
    try:
        con = pymysql.connect(**config)
        print('Connected')
        return con.cursor()

    except Exception as e:
        print(f'Database connection could not be established {e}')