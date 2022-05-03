from app import app
import urllib.request,json
from .models import articles
from .models import sources

Articles = articles.Articles
Sources = sources.Sources

# get api key
api_key = app.config['NEWS_API_KEY']

# get news base url
base_url = app.config['NEWS_API_BASE_URL']

# get articles base url
base_url_art = app.config['ARTICLES_API_BASE_URL']