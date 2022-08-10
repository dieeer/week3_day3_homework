from flask import Flask
from models.orders import Order
from models.orders_list import *

app = Flask(__name__)

from controllers import controller

if __name__ == "__main__":
    app.run(debug=True)