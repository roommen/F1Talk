import MySQLdb
from connection_string import cnx_str


def insert_race_result(race_results):
    connection = MySQLdb.connect(cnx_str['host'], cnx_str['username'], cnx_str['password'], cnx_str['db'])

    query = "INSERT INTO race_results(driver_name, circuit_name, position, year) VALUES(%s, %s, %s, %s)"
    print("Data inserted into the table race_results successfully.")
    try:
        cursor = connection.cursor()
        cursor.executemany(query, race_results)
        connection.commit()
    except:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()


def main():
    race_results = [('Sebastian Vettel', 'Australia', '1', '2017'),
                    ('Sebastian Vettel', 'China', '2', '2017'),
                    ('Sebastian Vettel', 'Bahrain', '1', '2017')]
    insert_race_result(race_results)


if __name__ == '__main__':
    main()
