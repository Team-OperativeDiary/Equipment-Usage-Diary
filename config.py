import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    #connection string poistettu
    SQLALCHEMY_TRACK_MODIFICATIONS = False


