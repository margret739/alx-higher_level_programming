#!/usr/bin/python3
""" Creates the state "Carlifonia" with the City "San Fransisco" from a D8 """

import sys
from relationship_state import Base.state
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]).
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
