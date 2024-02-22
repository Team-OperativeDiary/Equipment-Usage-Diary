from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Vehicle 
from app.models import MaintenanceItem
from config import Config

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return 'Welcome to the Vehicle Maintenance App!'

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get form data
        vehicle_name = request.form['name']
        
        # Create Vehicle object
        vehicle = Vehicle(name=vehicle_name)
        db.session.add(vehicle)
        db.session.commit()

        # date = request.form['date']
        # driving_hours = request.form['driving_hours']
        # oil_checked = request.form.get('oil_checked') == 'on'
        oil_added_amount = request.form['oil_added_amount']
        # Add other form fields similarly
        
        # Create MaintenanceItem object

        # date=date, driving_hours=driving_hours, oil_checked=oil_checked,
        maintenance_item = MaintenanceItem(oil_added_amount=oil_added_amount)
        
        # Add more fields as needed
        
        db.session.add(maintenance_item)
        db.session.commit()

        return redirect(url_for('main.index'))  # Redirect to homepage after submission

    return render_template('form.html')
