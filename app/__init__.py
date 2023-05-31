from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# You can define additional routes and view functions here.

if __name__ == '__main__':
    app.run()
