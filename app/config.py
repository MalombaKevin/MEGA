import os

class Config:
    SECRET_KEY="megaminds"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:megamind@localhost/megapitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",)


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}