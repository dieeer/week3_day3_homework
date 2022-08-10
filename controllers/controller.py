from flask import render_template
from app import app
from models.orders import Order
from models.orders_list import *

# @app.route('/')
# def index():
#     return "Hello World!"

@app.route('/')
def index():
    return render_template('index.html', title='customer orders', orders=orders)

