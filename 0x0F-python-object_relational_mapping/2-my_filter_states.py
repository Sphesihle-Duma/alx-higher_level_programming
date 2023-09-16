#!/usr/bin/python3
"""
    A script that searches an name
    from the database. The name is
    passed as an argument in the
    script.
    Args:
       mysql username: user of the mysql
       mysql password: password of the user
       database name: the name of the database
       state name: name of the state to search
"""
import MySQLdb
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    pt = 3306
    host = "localhost"
    db_conn = MySQLdb.connect(host=host, user=user, passwd=passwd,
                              db=db, port=pt)
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states \
                WHERE CONVERT(name USING latin1) \
                COLLATE Latin1_General_CS = '{}';".format(state_name))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db_conn.close()
