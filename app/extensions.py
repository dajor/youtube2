from spaces import Client 
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_bcrypt     import Bcrypt
from flask_babel import Babel


client = Client(
  region_name = 'fra1', # Required
  space_name = 'ideasondemand', # Optional, can be set in spaces/env.yaml and/or be updated with <client>.set_space(space_name)
  public_key = 'JKJ7FQRGCKWPIJA6L7NY', # Required, but can set key in spaces/env.yaml                                                                         
  secret_key = 'X582MPNC478TV+uGHpTQ2wytRu00BSB/1kCC8yYiXIM', # Required, but can set key in spaces/env.yaml

  # If any of region_name, public_key or secret_key are not provided, Client will override all values with env.yaml values.

)

db = SQLAlchemy  () # flask-sqlalchemy
bc = Bcrypt      () # flask-bcrypt

lm = LoginManager(   ) # flask-loginmanager

babel = Babel()