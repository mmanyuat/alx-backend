#!/usr/bin/env python3
"""Importing modules to start the flask-babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LOCALES = ['en', 'fr', 'es']

user_settings = {
    'user_id': 1,
    'preferred_locale': 'fr'  
}

@app.route('/')
def index():
    return render_template('6-index.html')

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale
    
    user_locale = user_settings.get('preferred_locale')
    if user_locale in SUPPORTED_LOCALES:
        return user_locale
    
    locale = request.accept_languages.best_match(SUPPORTED_LOCALES)
    if locale:
        return locale
    
    return 'en'

if __name__ == '__main__':
    app.run(debug=True)

