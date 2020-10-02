import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY=os.environ.get("42ff49abe2dd44e08eb28ab10b3103a6")
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey=42ff49abe2dd44e08eb28ab10b3103a6'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey=42ff49abe2dd44e08eb28ab10b3103a6'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}