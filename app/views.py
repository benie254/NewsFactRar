from flask import render_template
from app import app
from .requests import get_headlines,get_sources,get_articles,get_bbc,get_cnn,get_tech,get_tradar,get_verge

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
    my_bbc = get_bbc()

    print(my_bbc)

    return render_template('bbc.html',title=title,my_bbc=my_bbc)


@app.route('/cnn')
def cnn():
    """
    :return: cnn page + data
    """

    title = 'CNN News'
    my_cnn = get_cnn()

    print(my_cnn)

    return render_template('cnn.html',title=title,my_cnn=my_cnn)


@app.route('/techC')
def techC():
    """
    :return: Techcrunch page + data
    """

    title = 'TechCrunch'
    my_tech = get_tech()

    print(my_tech)

    return render_template('techC.html',title=title,my_tech=my_tech)


@app.route('/tRadar')
def tRadar():
    """
    :return: Techradar page + data
    """

    title = 'TechRadar'
    my_tradar = get_tradar()

    print(my_tradar)

    return render_template('tRadar.html',title=title,my_tradar=my_tradar)


@app.route('/verge')
def verge():
    """
    :return: the-verge page + data
    """

    title = 'The Verge'
    my_verge = get_verge()

    return render_template('verge.html',title=title,my_verge=my_verge)