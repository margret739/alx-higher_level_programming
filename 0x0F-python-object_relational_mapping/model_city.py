#!/usr/bin/python3
""" contains class definition of a statement """

from model_state import Base
from sqlalchemy import Column, integer, String, foreignmaker
from sqlalchemy.ext.declarative import declarative import declarative_base

class City(Bae):
    """
    class that defines each city """

    __tablename__ = 'cities'
    id = Column(integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey("States.id"), nullable=False)
