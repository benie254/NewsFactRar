from app import app
import urllib.request,json
from .models import articles
from .models import sources
from newsapi import NewsApiClient

Articles = articles.Articles
Sources = sources.Sources

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

    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=' + api_key

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_sources_results(source_results_list)

    return source_results