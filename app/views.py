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


@app.route('/articles')
def articles():
    """
    :return: articles page + data
    """

    title = 'All Articles'

    return render_template('articles.html',title=title)


@app.route('/bbc')
def bbc():
    """
    :return: bbc page + data
    """

    title = 'BBC News'

    return render_template('bbc.html',title=title)


@app.route('/cnn')
def cnn():
    """
    :return: cnn page + data
    """

    title = 'CNN News'

    return render_template('cnn.html',title=title)
