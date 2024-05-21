
CREATE DATABASE IF NOT EXISTS EUDb;
USE EUDb;


CREATE TABLE Category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Vehicle (
    vehicle_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    category_id INT,
    hasOil BOOLEAN DEFAULT FALSE,
    hasHydraulicOil BOOLEAN DEFAULT FALSE,
    hasGearOil BOOLEAN DEFAULT FALSE,
    hasLiquidCoolant BOOLEAN DEFAULT FALSE,
    hasGreasingCheck BOOLEAN DEFAULT FALSE,
    hasAutoGreaserDate BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE VehicleDiaryEntry (
    entry_id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_id INT,
    username VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
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
    automatic_greaser_last_date_filled DATE,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id)
);
-- Insert data into Vehicle table
INSERT INTO Vehicle (name) VALUES
('JCB JS 210 LC -11'),
('JCB JS 210 LC -18'),
('Liebherr R 920 -14'),
('New Holland 135 SR -08'),
('New Holland 135 BSR-2 -10'),
('New Holland 135 BSR-2 -10'),
('Caterpillar M 313 -15'),
('Caterpillar M315 -99'),
('JCB JS 160 W -12'),
('Wacker Neuson EW 100 -15'),
('Cat 308E2 -17'),
('ECM ES 85 SB4 -18'),
('Volvo EC 35 -02'),
('Sunward 80 -13'),
('Volvo DR 25 A -97'),
('Volvo DR 5350 -84'),
('Atlast AR 60 -06'),
('Hyundai 740 HL TM3 -02'),
('Volvo 110 F -08'),
('Volvo L30 D-Z -01'),
('JCB Robot -03'),
('JCB 421'),
('Lännen 860S -99'),
('Caterpillar D 4 Puskutraktori'),
('New Holland TL 100A Traktori'),
('John Deere 6534 Traktori'),
('Lännen AH 162 Tiehöylä, runko-ohjaus'),
('Scania G142 Tienhoitovarustus');
-- Insert data into VehicleDiaryEntry table
DELIMITER $$

CREATE PROCEDURE GenerateDummyData()
BEGIN
    DECLARE i INT DEFAULT 0;
    
    WHILE i < 100 DO
        INSERT INTO VehicleDiaryEntry (
            vehicle_id,
            username,
            date,
            driving_hours,
            oil_checked,
            oil_added_amount,
            hydraulic_oil_checked,
            hydraulic_oil_added_amount,
            gear_oil_checked,
            gear_oil_added_amount,
            liquid_coolant_checked,
            liquid_coolant_added_amount,
            fuel_added,
            fuel_type,
            greasing_checked,
            automatic_greaser_checked,
            automatic_greaser_last_date_filled
        )
        VALUES (
            FLOOR(RAND() * 27) + 1, -- Random vehicle_id between 1 and 27
            CONCAT('user', FLOOR(RAND() * 10)), -- Random username
            DATE_SUB(CURRENT_DATE(), INTERVAL FLOOR(RAND() * 365) DAY), -- Random date within the past year
            RAND() * 24, -- Random driving hours between 0 and 24
            RAND() > 0.5, -- Random oil_checked boolean
            RAND() * 10, -- Random oil_added_amount between 0 and 10
            RAND() > 0.5, -- Random hydraulic_oil_checked boolean
            RAND() * 10, -- Random hydraulic_oil_added_amount between 0 and 10
            RAND() > 0.5, -- Random gear_oil_checked boolean
            RAND() * 10, -- Random gear_oil_added_amount between 0 and 10
            RAND() > 0.5, -- Random liquid_coolant_checked boolean
            RAND() * 10, -- Random liquid_coolant_added_amount between 0 and 10
            RAND() * 100, -- Random fuel_added amount
            IF(RAND() > 0.5, 'Gasoline', 'Diesel'), -- Random fuel_type
            RAND() > 0.5, -- Random greasing_checked boolean
            RAND() > 0.5, -- Random automatic_greaser_checked boolean
            DATE_SUB(CURRENT_DATE(), INTERVAL FLOOR(RAND() * 365) DAY) -- Random automatic_greaser_last_date_filled within the past year
        );
        
        SET i = i + 1;
    END WHILE;
END$$

DELIMITER ;

CALL GenerateDummyData();
