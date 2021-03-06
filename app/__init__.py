from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()


def create_app(config_name):

    # initialize app
    app = Flask(__name__)

    # set up config
    app.config.from_object(config_options[config_name])

    # initialize flask extension
    bootstrap.init_app(app)

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # set config
    from .requests import configure_request
    configure_request(app)

    return app

# initialize Flask Extensions


from .main import errors, views
