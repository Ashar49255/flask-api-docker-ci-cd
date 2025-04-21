# app/routes.py
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Welcome to my Flask API!"})

@main.route('/products')
def get_products():
    return jsonify({"products": ["item1", "item2"]})
