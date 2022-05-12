import os

class Config:
    SECRET_KEY = "megaminds"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:megamind@localhost/mega'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME='kevinmalomba014@gmail.com'
    # MAIL_PASSWORD='malomba28'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}