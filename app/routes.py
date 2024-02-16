from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Vehicle, VehicleDiaryEntry
from config import Config

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return 'Welcome to the Vehicle Maintenance App!'

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get form data
        form_data = request.form
        vehicle_name = form_data['name']
        # Other form fields...
        
        # Create Vehicle object
        vehicle = Vehicle(name=vehicle_name)
        db.session.add(vehicle)
        db.session.commit()

        # Create VehicleDiaryEntry object
        entry = VehicleDiaryEntry(
            vehicle_id=vehicle.id,
            date=form_data['date'],
            driving_hours=form_data['driving_hours'],
            oil_checked=form_data.get('oil_checked') == 'on',
            oil_added_amount=form_data.get('oil_added_amount'),
            hydraulic_oil_checked=form_data.get('hydraulic_oil_checked') == 'on',
            hydraulic_oil_added_amount=form_data.get('hydraulic_oil_added_amount'),
            gear_oil_checked=form_data.get('gear_oil_checked') == 'on',
            gear_oil_added_amount=form_data.get('gear_oil_added_amount'),
            liquid_coolant_checked=form_data.get('liquid_coolant_checked') == 'on',
            liquid_coolant_added_amount=form_data.get('liquid_coolant_added_amount'),
            fuel_added=form_data.get('fuel_added'),
            fuel_type=form_data.get('fuel_type'),
            greasing_checked=form_data.get('greasing_checked') == 'on',
            automatic_greaser_checked=form_data.get('automatic_greaser_checked') == 'on',
            automatic_greaser_last_date_filled=form_data.get('automatic_greaser_last_date_filled')
        )
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('main.form'))  # Redirect to clear the form after submission
    return render_template('form.html')
