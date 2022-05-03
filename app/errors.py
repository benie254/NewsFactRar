from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    """
    :param error: function
    :return: render 404 error page
    """

    return render_template('fourOwfour.html'), 404