#How do you handle errors in Flask (e.g., 404)
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the homepage!"


@app.errorhandler(404)
def page_not_found(e):
    return render_template_string('''
        <h1>404 Error</h1>
        <p>Oops! The page you requested was not found.</p>
        <a href="/">Go back home</a>
    '''), 404

if __name__ == '__main__':
    app.run(debug=True)
