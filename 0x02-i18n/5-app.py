#!/usr/bin/python3
"""importing module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Retrieve user information based on 'login_as' parameter."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

@app.before_request
def before_request():
    """Set user information in global context before each request."""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """Select the best matching locale from the user's preferences."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

