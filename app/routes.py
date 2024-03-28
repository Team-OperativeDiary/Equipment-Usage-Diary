from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import MaintenanceItem
from app.models import Vehicle
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def main_page():
    return render_template('main_page.html', machines=machines)


machines = [
    {"name": "JCB JS 210 LC -11", "url": "/jcb-js-210-lc-11", "category": "Tela-alustaiset"},
    {"name": "JCB JS 210 LC -18", "url": "/jcb-js-210-lc-18", "category": "Tela-alustaiset"},
    {"name": "Liebherr R 920 -14", "url": "/liebherr-r-920-14", "category": "Tela-alustaiset"},
    {"name": "New Holland 135 SR -08", "url": "/new-holland-135-sr-08", "category": "Tela-alustaiset"},
    {"name": "New Holland 135 BSR-2 -10", "url": "/new-holland-135-bsr-2-10", "category": "Tela-alustaiset"},
    {"name": "Caterpillar M 313 -15", "url": "/caterpillar-m-313-15", "category": "Pyöräalustaiset"},
    {"name": "Caterpillar M315 -99", "url": "/caterpillar-m315-99", "category": "Pyöräalustaiset"},
    {"name": "JCB JS 160 W -12", "url": "/jcb-js-160-w-12", "category": "Pyöräalustaiset"},
    {"name": "Wacker Neuson EW 100 -15", "url": "/wacker-neuson-ew-100-15", "category": "Pyöräalustaiset"},
    {"name": "Cat 308E2 -17", "url": "/cat-308e2-17", "category": "Mini/midikaivukoneet"},
    {"name": "ECM ES 85 SB4 -18", "url": "/ecm-es-85-sb4-18", "category": "Mini/midikaivukoneet"},
    {"name": "Volvo EC 35 -02", "url": "/volvo-ec-35-02", "category": "Mini/midikaivukoneet"},
    {"name": "Sunward 80 -13", "url": "/sunward-80-13", "category": "Mini/midikaivukoneet"},
    {"name": "Volvo DR 25 A -97", "url": "/volvo-dr-25-a-97", "category": "Liikennetraktorit"},
    {"name": "Volvo DR 5350 -84", "url": "/volvo-dr-5350-84", "category": "Liikennetraktorit"},
    {"name": "Atlast AR 60 -06", "url": "/atlast-ar-60-06", "category": "kuormauskoneet"},
    {"name": "Hyundai 740 HL TM3 -02", "url": "/hyundai-740-hl-tm3-02", "category": "kuormauskoneet"},
    {"name": "Volvo 110 F -08", "url": "/volvo-110-f-08", "category": "kuormauskoneet"},
    {"name": "Volvo L30 D-Z -01", "url": "/volvo-l30-d-z-01", "category": "kuormauskoneet"},
    {"name": "JCB Robot -03", "url": "/jcb-robot-03", "category": "kuormauskoneet"},
    {"name": "JCB 421", "url": "/jcb-421", "category": "kuormauskoneet"},
    {"name": "Lännen 860S -99", "url": "/lannen-860s-99", "category": "Kaivurikuormaajat"},
    {"name": "Caterpillar D 4 Puskutraktori", "url": "/caterpillar-d-4-puskutraktori", "category": "Muut maarakkenuskoneet"},
    {"name": "New Holland TL 100A Traktori", "url": "/new-holland-tl-100a-traktori", "category": "Muut maarakkenuskoneet"},
    {"name": "John Deere 6534 Traktori", "url": "/john-deere-6534-traktori", "category": "Muut maarakkenuskoneet"},
    {"name": "Lännen AH 162 Tiehöylä, runko-ohjaus", "url": "/lannen-ah-162-tiehoyla-runko-ohjaus", "category": "Muut maarakkenuskoneet"},
    {"name": "Scania G142 Tienhoitovarustus", "url": "/scania-g142-tienhoitovarustus", "category": "Autot"},
]


class MaintenanceForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    date = DateField('Date', validators=[DataRequired()])
    driving_hours = IntegerField('Driving Hours', validators=[DataRequired(), NumberRange(min=0)])
    oil_checked = BooleanField('Oil Checked')
    oil_added_amount = IntegerField('Oil Added Amount', validators=[NumberRange(min=0)])
    hydraulic_oil_checked = BooleanField('Hydraulic Oil Checked')
    hydraulic_oil_added_amount = IntegerField('Hydraulic Oil Added Amount', validators=[NumberRange(min=0)])
    gear_oil_checked = BooleanField('Gear Oil Checked')
    gear_oil_added_amount = IntegerField('Gear Oil Added Amount', validators=[NumberRange(min=0)])
    liquid_coolant_checked = BooleanField('Liquid Coolant Checked')
    liquid_coolant_added_amount = IntegerField('Liquid Coolant Added Amount', validators=[NumberRange(min=0)])
    fuel_added = IntegerField('Fuel Added', validators=[NumberRange(min=0)])
    greasing_checked = BooleanField('Greasing Checked')
    automatic_greaser_checked = BooleanField('Automatic Greaser Checked')
    automatic_greaser_last_date_filled = DateField('Automatic Greaser Last Date Filled')

@main_bp.route('/<category>/<machine_name>', methods=['GET', 'POST'])
def machine_details(category, machine_name):
    vehicle: Vehicle = db.session.query(Vehicle).filter_by(name=find_matching_vehicle_by_url("/" + machine_name)).first()
    form = MaintenanceForm()
            
    if request.method == 'POST':
        if form.validate_on_submit():
            # If the request method is POST and the form is valid, handle form submission
            # Get form data
            vehicle_id =  vehicle.vehicle_id
            username = form.username.data
            date = form.date.data
            driving_hours = form.driving_hours.data
            oil_checked = form.oil_checked.data
            oil_added_amount = form.oil_added_amount.data
            hydraulic_oil_checked = form.hydraulic_oil_checked.data
            hydraulic_oil_added_amount = form.hydraulic_oil_added_amount.data
            gear_oil_checked = form.gear_oil_checked.data
            gear_oil_added_amount = form.gear_oil_added_amount.data
            liquid_coolant_checked = form.liquid_coolant_checked.data
            liquid_coolant_added_amount = form.liquid_coolant_added_amount.data
            fuel_added = form.fuel_added.data
            greasing_checked = form.greasing_checked.data
            automatic_greaser_checked = form.automatic_greaser_checked.data
            automatic_greaser_last_date_filled = form.automatic_greaser_last_date_filled.data

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
                automatic_greaser_last_date_filled=automatic_greaser_last_date_filled
            )
            db.session.add(maintenance_item)
            db.session.commit()
            # If the request method is POST and the form is valid, redirect to the results page
            return redirect(url_for('main.results'))
    else:
        # If the request method is GET, render the 'form.html' template with the provided category and machine_name
        return render_template('form.html', category=category, machine_name=machine_name, form=form)


@main_bp.route('/results')
def results():
    maintenance_items = MaintenanceItem.query.all()

    return render_template('results.html', maintenance_items=maintenance_items)




@main_bp.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):

    item = MaintenanceItem.query.get_or_404(item_id)
    
    db.session.delete(item)
    db.session.commit()
    
    return redirect(url_for('main.results'))

def find_matching_vehicle_by_url(url):
    for vehicle in machines:
        if vehicle['url'] == url:
            return vehicle['name']
    return None