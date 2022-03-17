# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 

# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory,send_file, after_this_request
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound
import re
from pytube import YouTube
# App modules
from app        import app, lm, db, bc
from app.models import Users
from app.forms  import LoginForm, RegisterForm, Youtube

# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Logout user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register a new user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    
    # declare the Registration Form
    form = RegisterForm(request.form)

    msg     = None
    success = False

    if request.method == 'GET': 

        return render_template( 'accounts/register.html', form=form, msg=msg )

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 
        email    = request.form.get('email'   , '', type=str) 

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = Users.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'
        
        else:         

            pw_hash = bc.generate_password_hash(password)

            user = Users(username, email, pw_hash)

            user.save()

            msg     = 'User created successfully.'     
            success = True

    else:
        msg = 'Input error'     

    return render_template( 'accounts/register.html', form=form, msg=msg, success=success )

# Authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    
    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        if user:
            
            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template( 'accounts/login.html', form=form, msg=msg )


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Youtube(request.form)
    msg = None
    if request.method == 'GET': 

        return render_template( 'home/index.html', form=form)

    if form.validate_on_submit():
        # assign form data to variables
        youtube_link = request.form.get('youtube_link', '', type=str)
        print (youtube_link)
        x = re.search(r"^((http|https)\:\/\/)?(www\.youtube\.com|youtu\.?be)\/((watch\?v=)?([a-zA-Z0-9]{11}))(&.*)*$", youtube_link)
        print (x)
        if x == None:
            msg = "URL error - please use only a Youtube Link"

            
   
        file = YouTube(youtube_link).streams.filter(progressive=True, file_extension='mp4').first().download()

        @after_this_request
        def remove_file(response):
            os.remove(file)    
            return response
        return send_file(file,as_attachment=True)
    
    return render_template( 'home/index.html', form=form,msg=msg)
    
# App main route + generic routing

# @app.route('/<path>')
# def rest(path):
    

    
#     #if not current_user.is_authenticated:
#     #    return redirect(url_for('login'))
    
    

#     try:

#         if not path.endswith( '.html' ):
#             path += '.html'

#         # Serve the file (if exists) from app/templates/FILE.html
#         return render_template( 'home/' + path )
    
#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404
    
#     except:
#         return render_template('home/page-500.html'), 500

# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')
