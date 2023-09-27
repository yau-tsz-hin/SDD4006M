from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# You must keep the routes at the end.
from app import routes, errors