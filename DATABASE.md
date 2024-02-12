CREATE TABLE EquipmentDiaryEntry (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    operator_name VARCHAR(255) NOT NULL,
    driving_hours FLOAT,
    oil_checked BOOLEAN,
    oil_added_amount FLOAT,
    hydraulic_oil_checked BOOLEAN,
    hydraulic_oil_added_amount FLOAT,
    gear_oil_checked BOOLEAN,
    gear_oil_added_amount FLOAT,
    liquid_coolant_checked BOOLEAN,
    liquid_coolant_added_amount FLOAT,
    fuel_added FLOAT,
    fuel_type ENUM('Gasoline', 'Diesel'),
    greasing_checked BOOLEAN,
    automatic_greaser_checked BOOLEAN,
    automatic_greaser_last_date_filled DATE
);
