'''Up next is to write our models. Flask provides developers with the power and flexibility of 
the SQL Alchemy ORM to manage and query the application data. ORM stands for Object Relational Mapper, 
it is a tool that allows developers to store and retrieve data using object oriented approaches and 
solves the object-relational impedance mismatch.

Also, Flask-SQLAlchemy is an extension that provides support for SQLAlchemy ORM in the Flask framework.
'''

from enum import unique
from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

#Here lies the models that will be stored in the database, to access by the application
class Person(db.Model):
    #Puts table name in db called "users"
    __tablename__ = 'users'
    
    #table
    id = db.Column(db.Integer(), primary_key = True) #primary id of the user, id for the user column tab
    api_key = db.Column(db.String(250), unique =True) #basing api_key of the user for bypass in the app
    username = db.Column(db.String(250)) #indicated username 
  
    def __init__(self, username, api_key ):
        self.username = username
        self.api_key = api_key

    def __repr__(self):
        return '<id {}>'.format(self.id)
   
    def serialize(self):
        return {
        'id': self.id, 
        "username": self.username,
        "api_key": self.api_key,
        }



class History(db.Model):
    from datetime import datetime 
    #Puts table name in db called "history"
    __tablename__ = 'history'
    
    #table
    id = db.Column(db.Integer(), primary_key = True) #id for the history column table 
    person_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique = True) #connected to the user tab
    date_time = db.Column(db.DateTime(), nullable = False, default = datetime.utcnow()) #timestamp
    #measurements
    systolic_pressure = db.Column(db.Float())
    diastolic_pressure = db.Column(db.Float())
    heart_rate = db.Column(db.Float())
    

  
    def __init__(self,title,date_time, systolic_pressure, diastolic_pressure, person_id, heart_rate ):
        self.person_id = person_id
        self.date_time = date_time 
        self.systolic_pressure = systolic_pressure
        self.diastolic_pressure = diastolic_pressure
       

    def __repr__(self):
        return '<id {}>'.format(self.id) #sets the id in order, eg when a data is inputted
                                         #value turns to 1
    def serialize(self):
        return {
        "id": self.id,
        "person_id": self.person_id,
        "date_time": self.date_time,
        "systolic_pressure": self.systolic_pressure,
        "diastolic_pressure": self.diastolic_pressure,
        "heart_rate": self.heart_rate
        }

class Maps(db.Model):
    #Puts table name in db called ""
    __tablename__ = 'maps'
    
    #table
    id = db.Column(db.Integer(), primary_key = True) #id for the maps table 
    map_id = db.Column(db.Integer, db.ForeignKey('users.id')) #connected to the user tab
    location = db.Column(db.String(50)) #location formatted in string type 
    nearby_locations = db.Column(db.String(50)) #nearby location of the given location formatted in string
    
    def __init__(self,map_id, location, nearby_locations ): #initialize values
        self.map_id = map_id
        self.location = location
        self.nearby_location = nearby_locations
       

    def __repr__(self):
        return '<id {}>'.format(self.id)
   
    def serialize(self): #json type values
        return {
        "id": self.id,
        "map_id": self.map_id,
        "location": self.location,
        "nearby_location": self.nearby_location
        }


