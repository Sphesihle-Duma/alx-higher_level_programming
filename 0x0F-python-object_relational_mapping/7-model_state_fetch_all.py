#!/usr/bin/python3
"""
    A script that lists all state objects from the database
    Args:
        mysql username: database user
        mysql password: password of the user
        database name: the database name
"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db_conn = create_engine('mysql://{}:{}@localhost:3306/{}'.
                            format(user, passwd,db),
                            pool_pre_ping=True)
    Session = sessionmaker(bind=db_conn)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
