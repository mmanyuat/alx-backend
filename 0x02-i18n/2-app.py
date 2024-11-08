#!/usr/bin/python3
"""Initializes modules flask, Babel"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """use request language to find the best match"""
    return request.accept.language.best.match(app.config['LANGUAGES'])

@app.route('/')

def index():
    """Display the welcome page"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)

