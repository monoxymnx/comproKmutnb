from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html leng="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Example</title>
</head>
<body>

    <h1>Hello, {{ name }}!</h1>
    <p>This is a simple Flask web application.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, name="Watchakorn")

@app.route('/greet/<username>')
def greet_user(username):
    return render_template_string(html_template, name=username)

if __name__ == '__main__':
    app.run(debug=True)