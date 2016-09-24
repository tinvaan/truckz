from flask import Blueprint, session, request, redirect, url_for, render_template, flash, abort

mod = Blueprint('journeys', __name__)

@mod.route('/journeys')
def journeys():
    return render_template('journeys/journeys.html')

@mod.route('/journeys/edit')
def edit_journeys():
    return "Work in progress"

@mod.route('/journeys/add', methods=['POST', 'GET'])
def add_journeys():
    return render_template('journeys/add_journeys.html')
