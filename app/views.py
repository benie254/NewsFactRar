from flask import render_template
from app import app

# views


@app.route('/')
def index():

    """
    :return: index page + data
    """

    return render_template('index.html')
