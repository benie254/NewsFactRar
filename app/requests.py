import urllib.request,json
from .models import Articles
from .models import Sources
from newsapi import NewsApiClient


def configure_request(app):
    global api_key,base_url,base_url_art,newsapi
    # get api key
    api_key = app.config['NEWS_API_KEY']
    # get news base url
    base_url = app.config['NEWS_API_BASE_URL']
    # get articles base url
    base_url_art = app.config['ARTICLES_API_BASE_URL']
    newsapi = NewsApiClient(api_key=api_key)


def get_headlines():
    """
    :return: response to NewsApiClient request
    """

    newsapi = NewsApiClient(api_key='cf03c3d8de3e48ffa0b0ed1f93681891')

    headlines = newsapi.get_top_headlines(language='en', sources='bbc-news, cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_headlines = headlines['articles']

    headlines_results = []

    source = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []

    for headline_item in range(len(all_headlines)):
        headline = all_headlines[headline_item]

        source.append(headline['source'])
        author.append(headline['author'])
        title.append(headline['title'])
        description.append(headline['description'])
        url.append(headline['url'])
        urlToImage.append(headline['urlToImage'])
        publishedAt.append(headline['publishedAt'])
        content.append(headline['content'])

        headline_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
        headlines_results.append(headline_object)

        contents = zip(source, author, title, description, url, urlToImage, publishedAt, content)

    return contents


def get_sources():
    """
    :return: request
    """

    get_sources_url = 'https://newsapi.org/v2/sources?language=en&apiKey=0f9d0d42be174a258e016c6403ddd477'

    'https://newsapi.org/v2/everything?q=us&from=2022-04-12&language=en&apiKey=0f9d0d42be174a258e016c6403ddd477'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_sources_results(source_results_list)

    return source_results


def process_sources_results(source_list):
    """
    :param source_list: function--process source results
    :return: list of source objects
    """

    source_results = []

    for source_item in source_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if name:
            source_object = Sources(name, description, url, category, country)
            source_results.append(source_object)

    return source_results


def get_articles():

    newsapi = NewsApiClient(api_key='0f9d0d42be174a258e016c6403ddd477')

    articles = newsapi.get_everything(language='en', sources='bbc-news, cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_articles = articles['articles']

    articles_results = []

    source = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []

    for article_item in range(len(all_articles)):
        article = all_articles[article_item]

        source.append(article['source'])
        author.append(article['author'])
        title.append(article['title'])
        description.append(article['description'])
        url.append(article['url'])
        urlToImage.append(article['urlToImage'])
        publishedAt.append(article['publishedAt'])
        content.append(article['content'])

        article_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
        articles_results.append(article_object)

        contents = zip(source, author, title, description, url, urlToImage, publishedAt, content)

    return contents


def get_bbc():

    newsapi = NewsApiClient(api_key='0f9d0d42be174a258e016c6403ddd477')

    g_bbc = newsapi.get_everything(sources='bbc-news', language='en')

    all_bbc = g_bbc['articles']

    bbc_results = []

    source = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []

    for bbc_item in range(len(all_bbc)):
        bbc = all_bbc[bbc_item]

        source.append(bbc['source'])
        author.append(bbc['author'])
        title.append(bbc['title'])
        description.append(bbc['description'])
        url.append(bbc['url'])
        urlToImage.append(bbc['urlToImage'])
        publishedAt.append(bbc['publishedAt'])
        content.append(bbc['content'])

        bbc_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
        bbc_results.append(bbc_object)

        contents = zip(source, author, title, description, url, urlToImage, publishedAt, content)

    return contents


def get_cnn():

    newsapi = NewsApiClient(api_key='0f9d0d42be174a258e016c6403ddd477')

    g_cnn = newsapi.get_everything(sources='cnn',language='en')

    all_cnn = g_cnn['articles']

    cnn_results = []

    source = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []

    for cnn_item in range(len(all_cnn)):
        cnn = all_cnn[cnn_item]

        source.append(cnn['source'])
        author.append(cnn['author'])
        title.append(cnn['title'])
        description.append(cnn['description'])
        url.append(cnn['url'])
        urlToImage.append(cnn['urlToImage'])
        publishedAt.append(cnn['publishedAt'])
        content.append(cnn['content'])

        cnn_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
        cnn_results.append(cnn_object)

        contents = zip(source, author, title, description, url, urlToImage, publishedAt, content)

    return contents


def get_tech():

    newsapi = NewsApiClient(api_key='0f9d0d42be174a258e016c6403ddd477')

    g_tech = newsapi.get_everything(sources='techcrunch',language='en')

    all_tech = g_tech['articles']

    tech_results = []

    source = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []

    for tech_item in range(len(all_tech)):
        tech = all_tech[tech_item]

        source.append(tech['source'])
        author.append(tech['author'])
        title.append(tech['title'])
        description.append(tech['description'])
        url.append(tech['url'])
        urlToImage.append(tech['urlToImage'])
        publishedAt.append(tech['publishedAt'])
        content.append(tech['content'])

        tech_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
        tech_results.append(tech_object)

        contents = zip(source, author, title, description, url, urlToImage, publishedAt, content)

    return contents


def get_tradar():

    newsapi = NewsApiClient(api_key='0f9d0d42be174a258e016c6403ddd477')

    g_tradar = newsapi.get_everything(sources='techradar', language='en')

    all_tradar = g_tradar['articles']

    tradar_results = []

    source = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []

    for tradar_item in range(len(all_tradar)):
        tradar = all_tradar[tradar_item]

        source.append(tradar['source'])
        author.append(tradar['author'])
        title.append(tradar['title'])
        description.append(tradar['description'])
        url.append(tradar['url'])
        urlToImage.append(tradar['urlToImage'])
        publishedAt.append(tradar['publishedAt'])
        content.append(tradar['content'])

        tradar_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
        tradar_results.append(tradar_object)

        contents = zip(source, author, title, description, url, urlToImage, publishedAt, content)

    return contents


def get_verge():

    newsapi = NewsApiClient(api_key='0f9d0d42be174a258e016c6403ddd477')

    g_verge = newsapi.get_everything(sources='the-verge',language='en')

    all_verge = g_verge['articles']

    verge_results = []

    source = []
    author = []
    title = []
    description = []
    url = []
    urlToImage = []
    publishedAt = []
    content = []

    for verge_item in range(len(all_verge)):
        verge = all_verge[verge_item]

        source.append(verge['source'])
        author.append(verge['author'])
        title.append(verge['title'])
        description.append(verge['description'])
        url.append(verge['url'])
        urlToImage.append(verge['urlToImage'])
        publishedAt.append(verge['publishedAt'])
        content.append(verge['content'])

        verge_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
        verge_results.append(verge_object)

        contents = zip(source, author, title, description, url, urlToImage, publishedAt, content)

    return contents