import sqlite3


def get_query_results(query):
    connection = sqlite3.connect('pairing_interview.db')
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()
