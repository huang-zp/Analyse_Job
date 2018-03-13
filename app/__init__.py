# coding: utf-8
import logging
import os
import pkgutil
import sys
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, jsonify, request, g, json
# from app.controllers.infomations import infomation
# from app.controllers.vulners import vulner
# from app.controllers.threats import threat

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)


def create_app():
    """Create Flask app."""

    app = Flask(__name__)
    config_app(app)
    # Register components
    # app.register_blueprint(infomation)
    # app.register_blueprint(vulner)
    # app.register_blueprint(threat)

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