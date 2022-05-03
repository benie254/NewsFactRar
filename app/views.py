from flask import render_template
from app import app
from .requests import get_headlines,get_sources,get_articles

# views


@app.route('/')
def index():

    """
    :return: index page + data
    """

    title = 'Welcome to NewsFactRar'

    my_headlines = get_headlines()
    my_sources = get_sources()

    print(my_headlines)
    print(my_sources)

    return render_template('index.html',title=title,my_headlines=my_headlines,my_sources=my_sources)


@app.route('/articles')
def articles():
    """
    :return: articles page + data
    """

    title = 'All Articles'
    my_articles = get_articles()

    print(my_articles)

    return render_template('articles.html',title=title,my_articles=my_articles)


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


@app.route('/verge')
def verge():
    """
    :return: the-verge page + data
    """

    title = 'The Verge'

    return render_template('verge.html',title=title)


@app.route('/techC')
def techC():
    """
    :return: Techcrunch page + data
    """

    title = 'TechCrunch'

    return render_template('techC.html',title=title)


@app.route('/tRadar')
def tRadar():
    """
    :return: Techradar page + data
    """

    title = 'TechRadar'

    return render_template('tRadar.html',title=title)
