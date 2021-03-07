
from flask_restful import Resource
from flask import request
from Model import db, Person, Maps

#From APP to GPS, then python to http, back to app 
#Gps location from the app, wtf how is the backend
#so like when I get the data, I should locate what's the nearest hospital from the location
#then extract the address and hospital's contact number
#yup extraction should be on the app
class Maps(Resource):
    #http
    def post():
        header = request.headers["Authorization"]
        json_data = request.get_json(force = True)

        if not header: 
            return {"Message": "No api key!"}, 400

        else: 
            user = Person.query.filter_by(api_key=header).first()

            if user:
                maps = Maps(
                    map_id = users.id,
                    location = json_data['location'],
                    nearby_location = json_data['nearby_location']
                )
                db.session.add(maps)
                db.session.commit()

                result = Maps.serialize(maps)
                return {"status": 'success', 'data': result}, 201 #success page
            
            else:
                return {"Messege" : "No user with that api key"}, 402 #error page 
    

    def get():
        result = []
        header = request.headers["Authorization"]

        if not header:
            return {"Messege" : "No api key!"}, 400
        else:
            user = Person.query.filter_by(api_key=header).first()
            
            if user:
                maps = Maps.query.filter_by(maps_id=users.id).all()

                for map in maps:
                    result.append(Maps.serialize(map))


            return {"status": 'success', 'data': result}, 201

class MapBackend():
    pass