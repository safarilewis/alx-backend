#!/usr/bin/env python3
"""Basic Flask app"""
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """routines before request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale"""
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The index page."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)