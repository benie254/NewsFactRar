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

    get_headlines = newsapi.get_top_headlines(language='en', sources='bbc-news, cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_headlines = get_headlines['articles']

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