from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask.ext.jsonpify import jsonify
from rest_declarative import ResultSensor1, ResultSensor2, Base

engine = create_engine('sqlite:///restDatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

app = Flask(__name__)
api = Api(app)

class Result1(Resource):
    def get(self):
        result1 = {'data': [dict(zip(tuple ("result 1") , session.query(ResultSensor1.resultSensor1).order_by('-id').first()))]}
        return jsonify(result1)

class Result2(Resource):
    def get(self):
        result2 = {'data': [dict(zip(tuple ("result 2") , session.query(ResultSensor2.resultSensor2).order_by('-id').first()))]}
        return jsonify(result2)
        
api.add_resource(Result1, '/result1')
api.add_resource(Result2, '/result2')

if __name__ == '__main__':
    app.run(port=5002)
