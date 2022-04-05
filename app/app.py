# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from flask            import Flask, request,g



# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(test_config=None):

    app = Flask(__name__)
    from .extensions import client, lm, db, bc,babel
    app.config.from_object('app.config.Config')


    

    with app.app_context():

        lm.init_app(app)       # init the login manager
        db.init_app(app)  
        bc.init_app(app)
        babel.init_app(app)

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
        from . import models
        from app.views import web1
        app.register_blueprint(web1)
    
        return app
