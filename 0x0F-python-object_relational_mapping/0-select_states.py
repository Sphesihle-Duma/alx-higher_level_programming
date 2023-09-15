#!/usr/bin/python3
""" A script that lists all states from the database
   Args:
       mysql username: username
       mysql password: password
       database name: database name
"""
import sys
import MySQLdb
if __name__ == "__main__":
    my_db = sys.argv[3]
    user = sys.argv[1]
    my_p = sys.argv[2]
    ht = "localhost"
    my_pt = 3306
    db = MySQLdb.connect(host=ht, user=user, passwd=my_p, db=my_db, port=my_pt)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    my_states = cur.fetchall()
    for state in my_states:
        print(state)
    cur.close()
    db.close()
