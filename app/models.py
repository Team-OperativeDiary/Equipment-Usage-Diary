from app import db

# class Vehicle(db.Model):
#     __tablename__ = 'Vehicle'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(100), nullable=False)



class MaintenanceItem(db.Model): # < placeholdername, should be VehicleDiaryEntry
    __tablename__ = 'VehicleDiaryEntry'
    entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
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
    fuel_type = db.Column(db.String(50))
    greasing_checked = db.Column(db.Boolean)
    automatic_greaser_checked = db.Column(db.Boolean)
    automatic_greaser_last_date_filled = db.Column(db.Date)