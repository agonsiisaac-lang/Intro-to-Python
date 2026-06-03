from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'Welcome to the Flask app!'

@app.route('/about')
def about():
    return 'This is a simple Flask application.'

@app.route('/login')
def login():
    return 'Login page'

@app.route('/contact')
def contact():
    return 'Contact us at 00089989'

if __name__ == "__main__":
    app.run(debug=True)

