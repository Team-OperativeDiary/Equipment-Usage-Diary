import os

class Config:
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # MySQL database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql://root:aDbGfCCd533Da-CHcfgdGf3-Cg1hH1FF@mysql.railway.internal:3306/railway'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug mode
    DEBUG = True
