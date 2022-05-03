from flask import Flask

# initialize app
app = Flask(__name__)

# set up config
app.config.from_object(DevConfig)

from app import views