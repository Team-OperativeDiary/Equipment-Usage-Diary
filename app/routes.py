from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import MaintenanceItem

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return 'Welcome to the Vehicle Maintenance App!'

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        date = request.form['date']
        driving_hours = request.form['drivingHours']
        oil_checked = 'oilChecked' in request.form
        oil_added_amount = request.form['oilAddedAmount']
        hydraulic_oil_checked = 'hydraulicOilChecked' in request.form
        hydraulic_oil_added_amount = request.form['hydraulicOilAddedAmount']
        gear_oil_checked = 'gearOilChecked' in request.form
        gear_oil_added_amount = request.form['gearOilAddedAmount']
        liquid_coolant_checked = 'liquidCoolantChecked' in request.form
        liquid_coolant_added_amount = request.form['liquidCoolantAddedAmount']
        fuel_added = request.form['fuelAdded']
        greasing_checked = 'greasingChecked' in request.form
        automatic_greaser_checked = 'automaticGreaserChecked' in request.form
        automatic_greaser_last_date_filled = request.form['automaticGreaserLastDateFilled']

        # Create MaintenanceItem object
        maintenance_item = MaintenanceItem(
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
            automatic_greaser_last_date_filled=automatic_greaser_last_date_filled
        )

        db.session.add(maintenance_item)
        db.session.commit()

        return redirect(url_for('main.results'))  # Redirect to results page after form submission

    return render_template('form.html')  # Render the form template for GET requests

@main_bp.route('/results')
def results():
    maintenance_items = MaintenanceItem.query.all()
    return render_template('results.html', maintenance_items=maintenance_items)


@main_bp.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    # Find the MaintenanceItem with the given item_id
    item = MaintenanceItem.query.get_or_404(item_id)
    
    # Delete the MaintenanceItem from the database
    db.session.delete(item)
    db.session.commit()
    
    # Redirect back to the results page
    return redirect(url_for('main.results'))