from flask import Flask, render_template, session, redirect, url_for
import qrcode
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# Generate a static token for the QR code
static_token = secrets.token_urlsafe(16)
app.config['STATIC_TOKEN'] = static_token

@app.route('/')
def index():
    return render_template('index.html', qr_code_url=f'/static/qr_code_{static_token}.png')

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    token = secrets.token_urlsafe(16)
    session['token'] = token
    qr = qrcode.make(f"http://127.0.0.1:5000/access/")
    qr.save(f'static/qr_code_{static_token}.png')
    return redirect(url_for('index'))

@app.route('/access', methods=['GET'])
def access_resource():
    token = session.pop('token', None)
    if token == app.config['STATIC_TOKEN']:
        return redirect(url_for('redirected'))
    else:
        return "Invalid Token. Access Denied."

@app.route('/redirected')
def redirected():
    return render_template('redirected.html')

if __name__ == '__main__':
    app.run(debug=True)
