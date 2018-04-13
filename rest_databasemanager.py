from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

#=============================================================================

from rest_declarative import PLCSensor1, PLCSensor2, Base
from rest_declarative import ResultSensor1, ResultSensor2

engine = create_engine('sqlite:///restDatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def PLCSensor1Handler(val):
    plcsensor1 = val
    dateandtime = ((datetime.datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"))
    
    new_sensor1value = PLCSensor1(valueSensor1 = str(plcsensor1), dateAndTime = str(dateandtime))
    session.add(new_sensor1value)
    session.commit()
    
def PLCSensor2Handler(val):
    plcsensor2 = val
    dateandtime = ((datetime.datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"))
    
    new_sensor2value = PLCSensor2(valueSensor2 = str(plcsensor2), dateAndTime = str(dateandtime))
    session.add(new_sensor2value)
    session.commit()
    
def ResultSensor1Handler(val):
    resultsensor1 = val
    dateandtime = ((datetime.datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"))
    
    new_sensor1result = ResultSensor1(resultSensor1 = str(resultsensor1), dateAndTime = str(dateandtime))
    session.add(new_sensor1result)
    session.commit()

def ResultSensor2Handler(val):
    resultsensor2 = val
    dateandtime = ((datetime.datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"))
    
    new_sensor2result = ResultSensor2(resultSensor2 = str(resultsensor2), dateAndTime = str(dateandtime))
    session.add(new_sensor2result)
    session.commit()
