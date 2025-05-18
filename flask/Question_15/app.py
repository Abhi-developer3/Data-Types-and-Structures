#How do you capture URL parameters in Flask?
from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'
if __name__ == '__main__':
    app.run(debug=True)