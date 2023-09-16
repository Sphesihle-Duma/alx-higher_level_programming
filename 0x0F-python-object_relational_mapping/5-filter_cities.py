#!/usr/bin/python3
""" A script that takes in the name of a state as an
    argument and lists all cities of that state
    Args:
        mysql username: database user
        mysql password: the password of the user
        database name: name of the database
        state name: name of the state
"""
import sys
import MySQLdb
if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbb = sys.argv[3]
    state_name = sys.argv[4]
    host = "localhost"
    port = 3306
    db_conn = MySQLdb.connect(host=host, user=user, passwd=passwd,
                              db=dbb, port=port)
    cur = db_conn.cursor()
    query = """ SELECT c.name FROM cities as c
                INNER JOIN states as s
                ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.id ASC
            """
    cur.execute(query, (state_name, ))
    cities = cur.fetchall()
    for city in cities:
        print(city[0], end=" ")
    cur.close()
    db_conn.close()
