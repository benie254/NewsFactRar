from flask import render_template
from . import main
from app.requests import get_headlines,get_sources,get_articles,get_bbc,get_cnn,get_tech,get_tradar,get_verge

# views


@main.route('/')
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


@main.route('/articles')
def articles():
    """
    :return: articles page + data
    """

    title = 'NewsFR-Articles'
    my_articles = get_articles()

    print(my_articles)

    return render_template('articles.html',title=title,my_articles=my_articles)


@main.route('/sources')
def sources():
    """
    :return: sources page + data
    """

    title = 'NewsFR-Sources'
    my_sources = get_sources()

    return render_template('sources.html',title=title,my_sources=my_sources)


@main.route('/bbc')
def bbc():
    """
    :return: bbc page + data
    """

    title = 'NewsFR-BBC'
    my_bbc = get_bbc()

    print(my_bbc)

    return render_template('bbc.html',title=title,my_bbc=my_bbc)


@main.route('/cnn')
def cnn():
    """
    :return: cnn page + data
    """

    title = 'NewsFR-News'
    my_cnn = get_cnn()

    print(my_cnn)

    return render_template('cnn.html',title=title,my_cnn=my_cnn)


@main.route('/techC')
def techC():
    """
    :return: Techcrunch page + data
    """

    title = 'NewsFR-TechCrunch'
    my_tech = get_tech()

    print(my_tech)

    return render_template('techC.html',title=title,my_tech=my_tech)


@main.route('/tRadar')
def tRadar():
    """
    :return: Techradar page + data
    """

    title = 'NewsFR-TechRadar'
    my_tradar = get_tradar()

    print(my_tradar)

    return render_template('tRadar.html',title=title,my_tradar=my_tradar)


@main.route('/verge')
def verge():
    """
    :return: the-verge page + data
    """

    title = 'NewsFR-TheVerge'
    my_verge = get_verge()

    return render_template('verge.html',title=title,my_verge=my_verge)