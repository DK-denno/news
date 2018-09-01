import os
class Config:
    '''
    stores api urls
    '''
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    API_KEY='e05ca232a09f4c6394d6716dbcde7fef'



class DevConfig(Config):
     '''
    these function pass in the Config class as a parameter
    '''
   
    pass


class ProdConfig(Config):
     '''
    these function pass in the Config class as a parameter
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}