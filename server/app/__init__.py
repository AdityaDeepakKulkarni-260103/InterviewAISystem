import os
import traceback
from importlib import import_module
import openai
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from werkzeug.middleware.proxy_fix import ProxyFix
from importlib import import_module
from app.api.models import *

db = SQLAlchemy()

try:
    openai.api_key = Config.OPENAI_API_KEY
    openai.api_type = Config.OPENAI_API_TYPE
    openai.resource_endpoint = Config.OPENAI_RESOURCE_ENDPOINT
    openai.api_version = Config.OPENAI_API_VERSION
    openai.gpt_engine = Config.OPENAI_GPT_ENGINE
except Exception as err:
    print(Exception,err)
    traceback.print_exc()

def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    for module_name in ():
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_database(app):
    with app.app_context():
        try:
            db.create_all()
        except Exception as err:
            print(Exception,err)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    register_extensions(app)
    app.wsgi_app = ProxyFix(app.wsgi_app,x_proto=1,x_host=1)
    register_blueprints(app)
    return app
