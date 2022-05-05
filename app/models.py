class Articles:
    """
    Class--define Articles objects
    """

    def __init__(self, source, author, title, description, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


class Sources:
    """
    Define Sources objects
    """

    def __init__(self,name,description,url,category,country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country