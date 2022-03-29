# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from flask            import Flask, request,g
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_bcrypt     import Bcrypt
from flask_babel import Babel
from spaces import Client 

client = Client(
  region_name = 'fra1', # Required
  space_name = 'ideasondemand', # Optional, can be set in spaces/env.yaml and/or be updated with <client>.set_space(space_name)
  public_key = 'JKJ7FQRGCKWPIJA6L7NY', # Required, but can set key in spaces/env.yaml                                                                         
  secret_key = 'X582MPNC478TV+uGHpTQ2wytRu00BSB/1kCC8yYiXIM', # Required, but can set key in spaces/env.yaml

  # If any of region_name, public_key or secret_key are not provided, Client will override all values with env.yaml values.

)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.config.Config')

db = SQLAlchemy  (app) # flask-sqlalchemy
bc = Bcrypt      (app) # flask-bcrypt

lm = LoginManager(   ) # flask-loginmanager
lm.init_app(app)       # init the login manager
babel = Babel(app)

# Setup database
@app.before_first_request
def initialize_database():
    
    db.create_all()
    from os.path import exists
    if exists("./downloads/invoice2data-296711-b48cf1290c2d.json") == False:
        client.list_files()
        client.download_file(
            file_name='invoice2data-296711-b48cf1290c2d.json',)
            #destination='', # Optional, should use a useful directory
            #space_name="ideasondemand" # Optional if a space is already set
        
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./downloads/invoice2data-296711-b48cf1290c2d.json"

@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code

# Import routing, models and Start the App
from app import views, models
