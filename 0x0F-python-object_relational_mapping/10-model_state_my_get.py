#!/usr/bin/python3
"""
    A script that prints the State object with the specified name
    Args:
    mysql username: database user
    mysql password: password of the user
    database name: the database name
    state name: the name of the state to search
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    db_conn = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Session = sessionmaker(bind=db_conn)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
