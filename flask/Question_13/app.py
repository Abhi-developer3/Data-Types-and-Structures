# How can you redirect with query parameters in Flask?
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/start')
def start():
    return redirect(url_for('greet', name='Abhishek', age=21))

@app.route('/greet')
def greet():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"Hello {name}, you are {age} years old."
if __name__ == '__main__':
    app.run(debug=True)
