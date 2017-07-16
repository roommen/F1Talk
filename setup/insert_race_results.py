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
                    ('Sebastian Vettel', 'Bahrain', '1', '2017'),
                    ('Sebastian Vettel', 'Russia', '2', '2017'),
                    ('Sebastian Vettel', 'Spain', '2', '2017'),
                    ('Sebastian Vettel', 'Monaco', '1', '2017'),
                    ('Sebastian Vettel', 'Canada', '4', '2017'),
                    ('Sebastian Vettel', 'Azerbaijan', '4', '2017'),
                    ('Lewis Hamilton', 'Australia', '2', '2017'),
                    ('Lewis Hamilton', 'China', '2', '2017'),
                    ('Lewis Hamilton', 'Bahrain', '2', '2017'),
                    ('Lewis Hamilton', 'Russia', '4', '2017'),
                    ('Lewis Hamilton', 'Spain', '1', '2017'),
                    ('Lewis Hamilton', 'Monaco', '7', '2017'),
                    ('Lewis Hamilton', 'Canada', '1', '2017'),
                    ('Lewis Hamilton', 'Azerbaijan', '5', '2017'),
                    ('Valtteri Bottas', 'Australia', '3', '2017'),
                    ('Valtteri Bottas', 'China', '6', '2017'),
                    ('Valtteri Bottas', 'Bahrain', '3', '2017'),
                    ('Valtteri Bottas', 'Russia', '1', '2017'),
                    ('Valtteri Bottas', 'Spain', 'Ret', '2017'),
                    ('Valtteri Bottas', 'Monaco', '4', '2017'),
                    ('Valtteri Bottas', 'Canada', '2', '2017'),
                    ('Valtteri Bottas', 'Azerbaijan', '2', '2017')
                    ]
    insert_race_result(race_results)


if __name__ == '__main__':
    main()
