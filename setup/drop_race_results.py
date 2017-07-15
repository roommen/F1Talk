import MySQLdb
from connection_string import cnx_str


def drop_race_results():
    connection = MySQLdb.connect(cnx_str['host'], cnx_str['username'], cnx_str['password'], cnx_str['db'])

    try:
        cursor = connection.cursor()

        cursor.execute('DROP TABLE race_results;')
        print("Table race_results dropped successfully.")
    except IndexError:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


def main():
    drop_race_results()


if __name__ == '__main__':
    main()

