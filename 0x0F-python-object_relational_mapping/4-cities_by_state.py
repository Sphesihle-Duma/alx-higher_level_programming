#!/usr/bin/python3
""" A script that lists all cities
    from the database
    Args:
        my username: database user
        my password: password of the database user
        database name: the name of the database
"""
import sys
import MySQLdb
if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    port = 3306
    db_conn = MySQLdb.connect(host=host, user=user, passwd=passwd,
                              db=db, port=port)
    cur = db_conn.cursor()
    query = """SELECT c.id, c.name, s.name FROM cities as c
               INNER JOIN states as s
               WHERE c.state_id = s.id
               ORDER BY c.id ASC
            """
    cur.execute(query)
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
    db_conn.close()
