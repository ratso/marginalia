# -*- coding: utf-8 -*-
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = False

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# SQLALCHEMY_DATABASE_URI = 'postgresql://cometp:qwerty@127.0.0.1:5432/marginalia'
DATABASE_CONNECT_OPTIONS = {}

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

PER_PAGE = 20

LANGUAGES = {
    'en': u'English',
    'ru': u'Русский'
}

BABEL_DEFAULT_LOCALE = 'ru'
BABEL_DEFAULT_TIMEZONE = 'Europe/Moscow'