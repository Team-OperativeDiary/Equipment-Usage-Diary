from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import MaintenanceItem

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def main_page():
    return render_template('main_page.html', machines=machines)

machines = [
    {"name": "JCB JS 210 LC -11", "url": "/jcb-js-210-lc-11"},
    {"name": "JCB JS 210 LC -18", "url": "/jcb-js-210-lc-18"},
    {"name": "Liebherr R 920 -14", "url": "/liebherr-r-920-14"},
    {"name": "New Holland 135 SR -08", "url": "/new-holland-135-sr-08"},
    {"name": "New Holland 135 BSR-2 -10", "url": "/new-holland-135-bsr-2-10"},
    {"name": "Pyöräalustaiset", "url": "/pyoraalustaiset"},
    {"name": "Caterpillar M 313 -15", "url": "/caterpillar-m-313-15"},
    {"name": "Caterpillar M315 -99", "url": "/caterpillar-m315-99"},
    {"name": "JCB JS 160 W -12", "url": "/jcb-js-160-w-12"},
    {"name": "Wacker Neuson EW 100 -15", "url": "/wacker-neuson-ew-100-15"},
    {"name": "Mini/midikaivukoneet", "url": "/mini-midikaivukoneet"},
    {"name": "Cat 308E2 -17", "url": "/cat-308e2-17"},
    {"name": "ECM ES 85 SB4 -18", "url": "/ecm-es-85-sb4-18"},
    {"name": "Volvo EC 35 -02", "url": "/volvo-ec-35-02"},
    {"name": "Sunward 80 -13", "url": "/sunward-80-13"},
    {"name": "Liikennetraktorit", "url": "/liikennetraktorit"},
    {"name": "Volvo DR 25 A -97", "url": "/volvo-dr-25-a-97"},
    {"name": "Volvo DR 5350 -84", "url": "/volvo-dr-5350-84"},
    {"name": "Pyöräkuormaajat ym. kuormauskoneet", "url": "/pyorakuormaajat-ym-kuormauskoneet"},
    {"name": "Atlast AR 60 -06", "url": "/atlast-ar-60-06"},
    {"name": "Hyundai 740 HL TM3 -02", "url": "/hyundai-740-hl-tm3-02"},
    {"name": "Volvo 110 F -08", "url": "/volvo-110-f-08"},
    {"name": "Volvo L30 D-Z -01", "url": "/volvo-l30-d-z-01"},
    {"name": "JCB Robot -03", "url": "/jcb-robot-03"},
    {"name": "JCB 421", "url": "/jcb-421"},
    {"name": "Kauvurikuormaajat", "url": "/kauvurikuormaajat"},
    {"name": "Lännen 860S -99", "url": "/lannen-860s-99"},
    {"name": "Muut maarakkenuskoneet", "url": "/muut-maarakkenuskoneet"},
    {"name": "Caterpillar D 4 Puskutraktori", "url": "/caterpillar-d-4-puskutraktori"},
    {"name": "New Holland TL 100A Traktori", "url": "/new-holland-tl-100a-traktori"},
    {"name": "John Deere 6534 Traktori", "url": "/john-deere-6534-traktori"},
    {"name": "Lännen AH 162 Tiehöylä, runko-ohjaus", "url": "/lannen-ah-162-tiehoyla-runko-ohjaus"},
    {"name": "Autot", "url": "/autot"},
    {"name": "Scania G142 Tienhoitovarustus", "url": "/scania-g142-tienhoitovarustus"},
]

@main_bp.route('/<string:machine_name>')
def machine_details(machine_name):
    # Your logic to retrieve machine details based on the machine_name
    return f"Details for machine: {machine_name}"

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

        return redirect(url_for('main.results'))  

    return render_template('form.html')  

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