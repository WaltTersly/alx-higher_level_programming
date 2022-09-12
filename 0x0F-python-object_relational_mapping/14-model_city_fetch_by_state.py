#!/usr/bin/python3
"""
prints all City objects from a database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    citiesState = session.query(City, State).filter(City.state_id == State.id)\
                                            .order_by(City.id).all()
    for city, state in citiesState:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
