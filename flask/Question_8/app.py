#  How do you manage sessions in Flask
from flask import Flask, session, redirect, url_for, request, render_template_string

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            session['username'] = username 
            return redirect(url_for('profile'))
        else:
            error = "Please enter a username."
            return render_template_string(LOGIN_HTML, error=error)
    return render_template_string(LOGIN_HTML)

@app.route('/profile')
def profile():
    username = session.get('username')
    if username:
        return f'''
            <h1>Welcome, {username}!</h1>
            <a href="{url_for('logout')}">Logout</a>
        '''
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

LOGIN_HTML = '''
    <h2>Login</h2>
    {% if error %}
    <p style="color:red;">{{ error }}</p>
    {% endif %}
    <form method="post">
        Username: <input type="text" name="username" /><br><br>
        <input type="submit" value="Login" />
    </form>
'''

if __name__ == '__main__':
    app.run(debug=True)

