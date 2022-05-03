class Config:
    """
    General configuration--parent class
    """

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey='
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?apiKey='

    pass


class ProdConfig(Config):
    """
    Production configuration--child class
    """

    pass


class DevConfig(Config):
    """
    Development configuration--child class
    """

    DEBUG = True
