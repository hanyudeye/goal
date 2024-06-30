# Sure! Let's start with Flask, a lightweight web framework for Python.
# First, make sure you have Flask installed. You can install it via pip if you haven't already:

# ```bash
# pip install Flask
# ```

# Now, let's create a simple Flask application:

# ```python
# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # Our "database"
# data = []

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         item = request.form['item']
#         data.append(item)
#         return redirect(url_for('display'))
#     return render_template('index.html')

# @app.route('/display')
# def display():
#     return render_template('display.html', data=data)

# if __name__ == '__main__':
#     app.run(debug=True)
# ```

# This code defines a Flask app with two routes:

# 1. The `/` route renders a form where users can submit data.
# 2. The `/display` route renders a page displaying the submitted data.

# Now, let's create the HTML templates.
# Create a folder named `templates` in your project directory, and inside it, create two HTML files: `index.html` and `display.html`.

# `index.html`:

# ```html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Submit Data</title>
# </head>
# <body>
#     <h1>Submit Data</h1>
#     <form method="post">
#         <input type="text" name="item" placeholder="Enter data">
#         <button type="submit">Submit</button>
#     </form>
# </body>
# </html>
# ```

# `display.html`:

# ```html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Display Data</title>
# </head>
# <body>
#     <h1>Submitted Data</h1>
#     <ul>
#         {% for item in data %}
#             <li>{{ item }}</li>
#         {% endfor %}
#     </ul>
#     <a href="/">Go back to submit more data</a>
# </body>
# </html>
# ```

# Now, you can run your Flask app by executing the Python script. Open your browser and go to `http://localhost:5000` to see the form, submit some data, and then see it displayed on the `/display` page.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

 # Our "database"
data = []

@app.route('/', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
         item = request.form['item']
         data.append(item)
         return redirect(url_for('display'))
     return render_template('index.html')

@app.route('/display')
def display():
     return render_template('display.html', data=data)

if __name__ == '__main__':
     app.run(debug=True)