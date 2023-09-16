#!/usr/bin/python3
""" A script that fetches data from database
    Args:
        username: user
        password: passwd
        db: database
"""
import MySQLdb
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    ps = sys.argv[2]
    db1 = sys.argv[3]
    pt = 3306
    ht = "localhost"
    db = MySQLdb.connect(host=ht, user=user, passwd=ps, db=db1, port=pt)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
    db.close()
