from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Hello, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
