#!/usr/bin/python3
"""
   Model_state module
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """
        State class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
