# redirected_website/app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/access/<user_token>', methods=['GET'])
def redirected_index(user_token):
    # Check if the user_token is valid
    if user_token:
        return render_template('redirected_index.html', user_token=user_token)
    else:
        return "Invalid Token. Access Denied."

if __name__ == '__main__':
    app.run(debug=True, port=5001)
