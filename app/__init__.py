from flask import Flask
from .config import DevConfig

# initialize app
app = Flask(__name__,instance_relative_config = True)

# set up config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views