from flask import render_template
from app import app

# @app.route('/')
# def index():
#     return "Hello World!"

@app.route('/orders')
def index():
    return render_template('index.html', title='customer orders', orders=orders)

