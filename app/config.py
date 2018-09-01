class Config:
    '''
    stores api urls
    '''
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'


class devConfig(Config):
    pass


class ProdConfig(Config):
    pass
