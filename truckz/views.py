from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    render_template('login.html')

@app.route('/trucks')
def trucks_list():
    return

#@app.route('/trucks/<str: id>')
#def truck():
#    return

@app.route('/owners')
def owners_list():
    return

#@app.route('/owners/<str: id>')
#def owner():
#    return

@app.route('/customers')
def customers_list():
    return

#@app.route('/customers/<str: id>')
#def customer():
#    return

