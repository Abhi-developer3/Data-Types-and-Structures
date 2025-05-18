# How do you return JSON responses in Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/user')
def get_user():
    return jsonify({
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    })
@app.route('/api/products')
def get_products():
    return jsonify([
        {"id": 1, "name": "Product 1", "price": 10.99},
        {"id": 2, "name": "Product 2", "price": 19.99}
    ])
if __name__ == '__main__':
    app.run(debug=True)