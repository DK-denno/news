import os
class Config:
    '''
    stores api urls
    '''
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    API_KEY='e05ca232a09f4c6394d6716dbcde7fef'



class DevConfig(Config):
  
   
    pass


class ProdConfig(Config):
     
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}