from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')

def index():
  
    return render_template('index.html')

@main.route('/megaminds')
@login_required
def megaminds():
    return render_template('megaminds.html')