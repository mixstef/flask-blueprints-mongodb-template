import os

from flask import Flask
from flask_pymongo import PyMongo

def create_app():
	
	app = Flask(__name__)
		
		
	# mongodb database name
	app.config['MONGO_DBNAME'] = os.environ.get('MY_APP_MONGODB_NAME',app.name)
	# configure mongo
	mongo.init_app(app)
	
	
	# common prefix for all routes in blueprints
	APP_URL_PREFIX = os.environ.get('MY_APP_PREFIX',None)
	# register all blueprints
	from .views import blueprints
	for bp in blueprints:
		app.register_blueprint(bp,url_prefix=APP_URL_PREFIX)
		
		
	return app

	
mongo = PyMongo()
app = create_app()	
	
