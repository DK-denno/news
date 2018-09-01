from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    #creating app configurations
    app.config.from_object(config_options[config_name])

    #initialising flask extensions
    bootstrap.init_app(app)

    #the init app method is called on a function to complete their initialisation

    #registering the blueprint created in app/__init__.py
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    return app
     