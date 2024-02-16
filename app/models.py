from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    entries = db.relationship('VehicleDiaryEntry', backref='vehicle', lazy=True)

class VehicleDiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    driving_hours = db.Column(db.Float)
    oil_checked = db.Column(db.Boolean)
    oil_added_amount = db.Column(db.Float)
    hydraulic_oil_checked = db.Column(db.Boolean)
    hydraulic_oil_added_amount = db.Column(db.Float)
    gear_oil_checked = db.Column(db.Boolean)
    gear_oil_added_amount = db.Column(db.Float)
    liquid_coolant_checked = db.Column(db.Boolean)
    liquid_coolant_added_amount = db.Column(db.Float)
    fuel_added = db.Column(db.Float)
    fuel_type = db.Column(db.Enum('Gasoline', 'Diesel'))
    greasing_checked = db.Column(db.Boolean)
    automatic_greaser_checked = db.Column(db.Boolean)
    automatic_greaser_last_date_filled = db.Column(db.Date)
