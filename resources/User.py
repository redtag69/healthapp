""" 
Referenced from Kalle Hallden's ToDo App 

Create usernames with unique id and api_key for temporary access 
"""

from flask_restful import Resource
from flask import request
from Model import db, Person

import random, string

class Register(Resource):

    def generate_key(self): #api_key generation
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(50))

    #Get data from Person db Model
    def get(self):
        users = Person.query.all()
        user_list = []
        for i in range(0, len(users)):
            user_list.append(users[i].serialize())
        return { "status" : str(user_list)}, 200

        
    #"Post data to Person db Model"
    def post(self):
        json_data = request.get_json(force=True)

        #If json_data = None, print No input data provided 
        if not json_data:
               return {'message': 'No input data provided'}, 400
      
        api_key = self.generate_key()

        user = Person.query.filter_by(api_key=api_key).first()
        
        #check for existing api key
        if user:
            return {'message': 'API key already exists'}, 400

        
        user = Person(
            username = json_data['username'],
            api_key = api_key
        )


        db.session.add(user)
        db.session.commit()

        result = Person.serialize(user)

        #If all parameters are passed, posts data to table 
        return { "status": 'success', 'data': result }, 201

    