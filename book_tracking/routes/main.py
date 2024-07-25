from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint, current_app, make_response
import services

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/getbooks', methods=['GET'])
def get_books():
    pass

@main_bp.route('/addbook', methods=['POST'])
def add_book():
    pass

@main_bp.route('/updatebook/<id>', methods=['PUT'])
def update_book(id):
    pass