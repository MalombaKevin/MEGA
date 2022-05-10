import os

class Config:
    SECRET_KEY = "megaminds"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:megamind@localhost/mega'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}