from flask import Flask, render_template_string

# HTML Jinja2 Template which will be shown in the browser
page_template = '''
        <div style="margin: auto; text-align: center;">
        <h1>Hello World!</h1>
        <h2>My first Acorn!</h2>
        </div>
        '''

# Defining the Flask Web App
app = Flask(__name__)

# Define the root path to display Hello World!
@app.route('/')
def root():
    return render_template_string(page_template)
