# How can you validate form data in Flask
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        if not username:
            error = "Username is required."
        elif not email or '@' not in email:
            error = "Valid email is required."

        if error:
            return render_template_string('<p>{{ error }}</p>', error=error)
        return "Form submitted successfully!"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
