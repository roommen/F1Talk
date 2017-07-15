import MySQLdb
from connection_string import cnx_str


def select_race_results():
    connection = MySQLdb.connect(cnx_str['host'], cnx_str['username'], cnx_str['password'], cnx_str['db'])

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * from race_results;')

        row = cursor.fetchone()

        print("Retrieving data from race_results")
        while row is not None:
            print(row)
            row = cursor.fetchone()
    except:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


def main():
    select_race_results()


if __name__ == '__main__':
    main()
