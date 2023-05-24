from flask import Flask

app = Flask(__name__)
#___________________________________

@app.route('/')
def index():
    return 'Hello, Flask!'


# You must keep the routes at the end.
from app import routes, errors