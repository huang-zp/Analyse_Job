# coding: utf-8
import logging
import os
import pkgutil
import sys
from logging.handlers import TimedRotatingFileHandler
from app.models import User, Role
from app.engines import db
from flask import Flask, jsonify, request, g, json
from app.controllers import company, message, datalog, data, aj, trend, jobtype, auth

from flask_login import LoginManager


project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

def create_app():
    """Create Flask app."""

    app = Flask(__name__)
    config_app(app)
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
    # Register components
    # app.register_blueprint(infomation)
    # app.register_blueprint(vulner)
    app.register_blueprint(aj)
    app.register_blueprint(company)
    app.register_blueprint(trend)
    app.register_blueprint(message)
    app.register_blueprint(jobtype)
    app.register_blueprint(data)
    app.register_blueprint(datalog)
    app.register_blueprint(auth)


    class NonASCIIJsonEncoder(json.JSONEncoder):
        def __init__(self, **kwargs):
            kwargs['ensure_ascii'] = False
            super(NonASCIIJsonEncoder, self).__init__(**kwargs)

    app.json_encoder = NonASCIIJsonEncoder

    return app




def config_app(app):
    from .config import load_config
    config = load_config()

    app.config.from_object(config)



