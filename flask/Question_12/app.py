#How do you define a custom Jinja filter in Flask
from flask import Flask, render_template

app = Flask(__name__)

# Define the custom filter function
def reverse_string(s):
    return s[::-1]

# Register the filter with Jinja
app.jinja_env.filters['reverse'] = reverse_string

# Example route rendering a template
@app.route('/')
def index():
    return render_template('index.html', text="Hello, PWskills")
if __name__ == '__main__':
    app.run(debug=True)