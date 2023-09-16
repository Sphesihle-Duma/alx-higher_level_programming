#!/usr/bin/python3
""" A script that searches a state from
    the database
    Args:
        mysql username: database user
        mysql password: password of the user
        mysql database: the database to be used
        state name: the name of the state
"""
import sys
import MySQLdb
if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    host = "localhost"
    pt = 3306
    db_conn = MySQLdb.connect(host=host, passwd=passwd, user=user,
                              db=db, port=pt)
    cur = db_conn.cursor()
    query = """ SELECT * FROM states
                WHERE name = %s
                ORDER BY id ASC
            """
    cur.execute(query, (state_name, ))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db_conn.close()
