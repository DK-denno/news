class Headlines:
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Sources:
    def __init__(self, id, name, url, country):

        self.id = id
        self.name = name
        self.url = url
        self.country = country
