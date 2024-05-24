from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

from app.routes import main_bp
app.register_blueprint(main_bp)