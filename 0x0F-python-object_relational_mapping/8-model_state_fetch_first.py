#!/usr/bin/python3
"""
    A script that prints the first state object from the database
    Args:
    mysql username: database user
    mysql password: password of the database
    database name : the name of the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db_conn = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Session = sessionmaker(bind=db_conn)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if not first_state:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
    session.close()
