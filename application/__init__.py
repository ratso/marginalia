# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.triangle import Triangle

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.url_map.strict_slashes = False


# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

Triangle(app)

from library import i18n

from frontend import front_module
app.register_blueprint(front_module, url_prefix='/')

from api import api_module
app.register_blueprint(api_module, url_prefix='/api')


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()