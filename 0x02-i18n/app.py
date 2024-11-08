#!/usr/bin/env python3
"""importing modules for the app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime, _
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

# Example of user settings for demonstration purposes
user_settings = {
    'user_id': 1,
    'preferred_locale': 'fr',
    'preferred_timezone': 'Europe/Paris'
}

SUPPORTED_LOCALES = ['en', 'fr']

@app.route('/')
def index():
    # Get the current time based on the selected timezone
    current_time = datetime.now(pytz.timezone(get_timezone()))
    formatted_time = format_datetime(current_time)

    # Pass translated message with formatted time to template
    message = _('The current time is %(current_time)s.', current_time=formatted_time)
    return render_template('index.html', message=message)

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale

    user_locale = user_settings.get('preferred_locale')
    if user_locale in SUPPORTED_LOCALES:
        return user_locale

    return request.accept_languages.best_match(SUPPORTED_LOCALES) or 'en'

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

