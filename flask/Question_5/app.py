# How can you generate URLs for routes in Flask using url_for
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<username>')
def profile(username):
    return f"Profile of {username}"

if __name__ == '__main__':
    app.run(debug=True)