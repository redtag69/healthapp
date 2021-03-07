'''Here, we have defined some configuration that the API will be using. 
We are also using the PostgreSQL database. If you prefer other databases,
you just have to modify the value accordingly.
'''

import os 
from access import username, password, localhost, database

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIF = False
SQLALCHEMY_DATABASE_URI= f"postgresql://{username}:{password}@{localhost}/{database}"

