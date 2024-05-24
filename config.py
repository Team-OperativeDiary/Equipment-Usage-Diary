import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    #yhdistäminen railway database urliin ei vielä onnistu
    SQLALCHEMY_TRACK_MODIFICATIONS = False


