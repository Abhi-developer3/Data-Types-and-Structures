# How do you handle forms in Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

    
        if not name or not email:
            return render_template('form.html', error="All fields are required!")

        return render_template('success.html', name=name, email=email)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
