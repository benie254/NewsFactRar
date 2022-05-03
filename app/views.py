from flask import render_template
from app import app

# views


@app.route('/')
def index():

    """
    :return: index page + data
    """

    title = 'Welcome to NewsFactRar'

    return render_template('index.html',title=title)
