# main_website/app.py
from flask import Flask, render_template, session, redirect, url_for
import qrcode
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# URL of the redirected website
redirected_website_url = "http://127.0.0.1:5001/"  # Update with your actual URL

# Generate a static token for the QR code
static_token = secrets.token_urlsafe(16)
app.config['STATIC_TOKEN'] = static_token

# Generate a unique token for each user
def generate_user_token():
    return secrets.token_urlsafe(16)

# Store user tokens in a set
app.config['USER_TOKENS'] = set()

# Generate the QR code with the user-specific token
def generate_qr_code(user_token):
    qr = qrcode.make(f"{redirected_website_url}/access/{user_token}")
    qr.save(f'static/qr_code_{static_token}.png')

@app.route('/')
def main_index():
    user_token = generate_user_token()
    session['user_token'] = user_token
    app.config['USER_TOKENS'].add(user_token)
    generate_qr_code(user_token)
    return render_template('main_index.html', qr_code_url=f'/static/qr_code_{static_token}.png')

@app.route('/access', methods=['GET'])
def access_resource():
    user_token = session.pop('user_token', None)
    if user_token in app.config['USER_TOKENS']:
        return redirect(url_for('redirected_index', user_token=user_token))
    else:
        return "Invalid Token. Access Denied."

if __name__ == '__main__':
    app.run(debug=True)
