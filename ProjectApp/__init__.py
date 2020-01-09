#!/usr/bin/env python3

# __init__.py for DotWatchAppWebsite

from flask import Flask#__ # double underscores are presumably a typo?
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import os, sys

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

# All login and database setup comes from this tutorial: https://scotch.io/tutorials/authentication-and-authorization-with-flask-login

def create_app():
	app = Flask(__name__)


	# if os.path.exists("/Users/parker"):
	# 	# running on personal testing computer, enable debug mode
	# 	app.debug = True
	# 	print("RUNNING '{}' IN DEBUG MODE".format(__name__))

	# 	# add the required paths for imports, but later

	# else:
	# 	app.debug = False



	app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'


	db.init_app(app)

	# Login Manager Chunk
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		# since the user_id is just the primary key of our user table, use it in the query for the user
		return User.query.get(int(user_id))

	

	# blueprint for auth routes in our app
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	# blueprint for non-auth parts of app
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app