import MySQLdb
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

cnx_str = {'host': 'f1.cemnrzna330w.ap-south-1.rds.amazonaws.com',
           'username': 'runcy',
           'password': 'enternow123',
           'db': 'f1'}


def lambda_handler(event, context):
    logger.debug('input from lex = {}'.format(event))
    results = event('results')

    connection = MySQLdb.connect(cnx_str['host'], cnx_str['username'], cnx_str['password'], cnx_str['db'])

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * from race_results;')

        row = cursor.fetchone()

        print("Retrieving data from race_results")
        while row is not None:
            print(row)
            row = cursor.fetchone()
    except IndexError:
        print('Unexpected error occurred')
    finally:
        cursor.close()
        connection.close()
