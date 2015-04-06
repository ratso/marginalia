# Import Babel
from flask import request, g
from flask.ext.babel import Babel
from application import app

babel = Babel(app)


@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
