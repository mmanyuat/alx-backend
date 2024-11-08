#!/usr/bin/env python3
"""Importing modules"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)

# Example of user settings dictionary for demonstration
user_settings = {
    'user_id': 1,
    'preferred_timezone': 'Europe/Paris'  # Example timezone for a user
}

@app.route('/')
def index():
    return render_template('7-index.html')

@babel.localeselector
def get_locale():
    # Locale selection logic (as described previously)
    locale = request.args.get('locale')
    if locale in ['en', 'fr', 'es']:
        return locale

    user_locale = user_settings.get('preferred_locale')
    if user_locale in ['en', 'fr', 'es']:
        return user_locale

    locale = request.accept_languages.best_match(['en', 'fr', 'es'])
    return locale or 'en'

@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone  
        except UnknownTimeZoneError:
            pass

    user_timezone = user_settings.get('preferred_timezone')
    if user_timezone:
        try:
            return pytz.timezone(user_timezone).zone  
        except UnknownTimeZoneError:
            pass  

    return 'UTC'
