import sqlite3


def get_query_results(query):
    connection = sqlite3.connect('pairing_interview.db')
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def get_raw_data():
    connection = sqlite3.connect('pairing_interview.db')
    cursor = connection.cursor()
    return [{"xValue": row[1], "yValue": row[2]} for row in cursor.execute("SELECT * FROM data")]
