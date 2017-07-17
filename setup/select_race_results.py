import MySQLdb
import logging
from connection_string import cnx_str

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def select_race_results():
    connection = MySQLdb.connect(cnx_str['host'], cnx_str['username'], cnx_str['password'], cnx_str['db'])

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT driver_name from race_results where race_results.year = "2017" AND '
                       'race_results.circuit_name = "Spain" AND race_results.position = "1";')
        row = cursor.fetchone()
        print(row)

        # cursor.execute('SELECT * from race_results;')
        # row = cursor.fetchone()
        # print("Retrieving data from race_results")
        # while row is not None:
        #     print(row)
        #     row = cursor.fetchone()
    except IndexError:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    select_race_results()
