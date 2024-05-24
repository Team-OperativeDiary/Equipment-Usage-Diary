from app import db

class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    hasOil = db.Column(db.Boolean, default=False, nullable=True)
    hasHydraulicOil = db.Column(db.Boolean, default=False, nullable=True)
    hasGearOil = db.Column(db.Boolean, default=False, nullable=True)
    hasLiquidCoolant = db.Column(db.Boolean, default=False, nullable=True)
    hasGreasingCheck = db.Column(db.Boolean, default=False, nullable=True)
    hasAutoGreaserDate = db.Column(db.Boolean, default=False, nullable=True)



class MaintenanceItem(db.Model): 
    __tablename__ = 'VehicleDiaryEntry'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicle_id = db.Column(db.String(191), db.ForeignKey('Vehicle.id'), nullable=False)
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
    automatic_greaser_last_date_filled = db.Column(db.Date)
    description = db.Column(db.String(2000))
    automatic_greaser_checked = db.Column(db.Boolean)





#     ALTER TABLE VehicleDiaryEntry
# DROP FOREIGN KEY VehicleDiaryEntry_vehicle_id_fkey;

# ALTER TABLE VehicleDiaryEntry
# ADD CONSTRAINT VehicleDiaryEntry_vehicle_id_fkey
# FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id)
# ON DELETE RESTRICT ON UPDATE CASCADE;




# -- Alter table to change id column type and set it as primary key with auto-increment
# ALTER TABLE `Vehicle`
# MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;

# -- Update foreign key references
# ALTER TABLE `MaintenanceReport`
# DROP FOREIGN KEY `MaintenanceReport_vehicle_id_fkey`,
# MODIFY COLUMN `vehicle_id` INT NOT NULL,
# ADD CONSTRAINT `fk_vehicle_id`
#   FOREIGN KEY (`vehicle_id`)
#   REFERENCES `Vehicle` (`id`)
#   ON DELETE RESTRICT
#   ON UPDATE CASCADE;

# ALTER TABLE `VehicleDiaryEntry`
# DROP FOREIGN KEY `VehicleDiaryEntry_vehicle_id_fkey`,
# MODIFY COLUMN `vehicle_id` INT NOT NULL,
# ADD CONSTRAINT `fk_vehicle_id`
#   FOREIGN KEY (`vehicle_id`)
#   REFERENCES `Vehicle` (`id`)
#   ON DELETE RESTRICT
#   ON UPDATE CASCADE;

# ALTER TABLE `vehiclefaultnotifications`
# DROP FOREIGN KEY `vehiclefaultnotifications_vehicle_id_fkey`,
# MODIFY COLUMN `vehicle_id` INT NOT NULL,
# ADD CONSTRAINT `fk_vehicle_id`
#   FOREIGN KEY (`vehicle_id`)
#   REFERENCES `Vehicle` (`id`)
#   ON DELETE RESTRICT
#   ON UPDATE CASCADE;
