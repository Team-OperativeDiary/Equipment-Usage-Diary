import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    #connection string poistettu jippii
    SQLALCHEMY_TRACK_MODIFICATIONS = False


