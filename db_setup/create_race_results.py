import MySQLdb
from connection_string import cnx_str


def create_race_results():
    connection = MySQLdb.connect(cnx_str['host'], cnx_str['username'], cnx_str['password'], cnx_str['db'])

    try:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE race_results(driver_name VARCHAR(255), circuit_name VARCHAR(255), position VARCHAR(3), year VARCHAR(5));')
        print("Table race_results created successfully.")
    except IndexError:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


def main():
    create_race_results()


if __name__ == '__main__':
    main()

