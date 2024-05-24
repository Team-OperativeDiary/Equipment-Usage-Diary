from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Category, MaintenanceItem, Vehicle
from sqlalchemy.orm.exc import NoResultFound


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def main_page():
    items = db.session.query(Vehicle.name, Category.name, Vehicle.model, Vehicle.year).join(Category, Vehicle.category_id == Category.id).all()
    
    categorized_items = {}
    
    for vehicle_name, category_name, vehicle_model, vehicle_year in items:
        if category_name not in categorized_items:
            categorized_items[category_name] = []
        # Generate URL by transforming the vehicle name
        vehicle_url = f"/{category_name.lower().replace(' ', '-')}/{vehicle_name.lower().replace(' ', '-')}"
        categorized_items[category_name].append({'name': vehicle_name, 'url': vehicle_url, 'model': vehicle_model, 'year': vehicle_year})
    
    return render_template('main_page.html', categorized_items=categorized_items)

def extract_name_and_model_from_url(url):
    # Remove leading and trailing slashes, then split at the first "-" occurrence
    parts = url.strip("/").split("-", 1)
    if len(parts) == 2:
        # Extract the name and model, replacing "-" with space
        name = parts[0]
        model = parts[1].replace("-", " ")
        return name, model
    else:
        return None, None


    
@main_bp.route('/<category>/<machine_name>', methods=['GET', 'POST'])
def machine_details(category, machine_name):
    name, model = extract_name_and_model_from_url(machine_name)

    vehicle: Vehicle = db.session.query(Vehicle).filter_by(name=machine_name).first()
    print(f"Name: {name}, Model: {model}")

   
            
    if request.method == 'POST':
        # If the request method is POST, handle form submission
        # Get form data
        vehicle_id = vehicle.id
        username = request.form['username']
        date = request.form['date']
        driving_hours = request.form['drivingHours']
        oil_checked = 'oilChecked' in request.form
        oil_added_amount = request.form['oilAddedAmount'] if 'oilAddedAmount' in request.form else None
        hydraulic_oil_checked = 'hydraulicOilChecked' in request.form
        hydraulic_oil_added_amount = request.form['hydraulicOilAddedAmount'] if 'hydraulicOilAddedAmount' in request.form else None
        gear_oil_checked = 'gearOilChecked' in request.form
        gear_oil_added_amount = request.form['gearOilAddedAmount'] if 'gearOilAddedAmount' in request.form else None
        liquid_coolant_checked = 'liquidCoolantChecked' in request.form
        liquid_coolant_added_amount = request.form['liquidCoolantAddedAmount'] if 'liquidCoolantAddedAmount' in request.form else None
        fuel_added = request.form['fuelAdded'] if 'fuelAdded' in request.form else None
        greasing_checked = 'greasingChecked' in request.form
        automatic_greaser_checked = 'automaticGreaserChecked' in request.form
        automatic_greaser_last_date_filled = request.form['automaticGreaserLastDateFilled'] if 'automaticGreaserLastDateFilled' in request.form else None
        description = request.form['description'] if 'description' in request.form else None

        # Create a MaintenanceItem object and add it to the database
        maintenance_item = MaintenanceItem( 
            vehicle_id=vehicle_id, 
            username=username,
            date=date,
            driving_hours=driving_hours,
            oil_checked=oil_checked,
            oil_added_amount=oil_added_amount,
            hydraulic_oil_checked=hydraulic_oil_checked,
            hydraulic_oil_added_amount=hydraulic_oil_added_amount,
            gear_oil_checked=gear_oil_checked,
            gear_oil_added_amount=gear_oil_added_amount,
            liquid_coolant_checked=liquid_coolant_checked,
            liquid_coolant_added_amount=liquid_coolant_added_amount,
            fuel_added=fuel_added,
            greasing_checked=greasing_checked,
            automatic_greaser_checked=automatic_greaser_checked,
            automatic_greaser_last_date_filled=automatic_greaser_last_date_filled,
            description=description
        )
        db.session.add(maintenance_item)
        db.session.commit()
        # If the request method is POST, redirect to the results page
        return redirect(url_for('main.results'))
    else:
        # If the request method is GET, render the 'form.html' template with the provided category and machine_name
        return render_template('form.html', category=category, machine_name=machine_name)

@main_bp.route('/results')
def results():
    maintenance_items = MaintenanceItem.query.all()
    
    # Print attributes of each maintenance item to the command line
    for item in maintenance_items:
        print(f"Username: {item.username}, Date: {item.date}, Driving Hours: {item.driving_hours}")
        # Add more attributes as needed
        
    return render_template('results.html', maintenance_items=maintenance_items)

@main_bp.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = MaintenanceItem.query.get_or_404(item_id)
    
    db.session.delete(item)
    db.session.commit()
    
    return redirect(url_for('main.results'))

