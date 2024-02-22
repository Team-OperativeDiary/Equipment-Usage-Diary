from app import db

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

