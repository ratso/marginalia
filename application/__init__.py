# Import flask and template operators
from flask import Flask, g, request

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import Babel
from flask.ext.babel import Babel
from config import LANGUAGES

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

babel = Babel(app)


@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(LANGUAGES.keys())

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from frontend import front_module
app.register_blueprint(front_module, url_prefix='/')

from api import api_module
app.register_blueprint(api_module, url_prefix='/api')


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()