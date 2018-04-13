from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class PLCSensor1(Base):
    __tablename__ = 'dataSensor1'
    id = Column(Integer, primary_key = True)
    dateAndTime = Column(String(50))
    valueSensor1 = Column(String(50))

class PLCSensor2(Base):
    __tablename__ = 'dataSensor2'
    id = Column(Integer, primary_key = True)
    dateAndTime = Column(String(50))
    valueSensor2 = Column(String(50))

class ResultSensor1(Base):
    __tablename__ = 'resultSensor1'
    id = Column(Integer, primary_key = True)
    dateAndTime = Column(String(50))
    resultSensor1 = Column(String(50))
    
class ResultSensor2(Base):
    __tablename__ = 'resultSensor2'
    id = Column(Integer, primary_key = True)
    dateAndTime = Column(String(50))
    resultSensor2 = Column(String(50))

engine = create_engine('sqlite:///restDatabase.db')

Base.metadata.create_all(engine)
