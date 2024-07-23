from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint, current_app, make_response
import services

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

