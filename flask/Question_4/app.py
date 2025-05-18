#How do you render HTML templates in Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Abhishek")

if __name__ == '__main__':
    app.run(debug=True)
