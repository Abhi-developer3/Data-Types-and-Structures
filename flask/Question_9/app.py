# How do you redirect to a different route in Flask
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the home page.'

@app.route('/go-to-home')
def go_to_home():
    return redirect(url_for('home'))  # Redirects to the 'home' route

if __name__ == '__main__':
    app.run(debug=True)
