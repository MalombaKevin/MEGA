from flask import render_template,redirect,url_for, abort

from app.models import User
from . import main
from flask_login import login_required

@main.route('/')

def index():
  
    return render_template('index.html')

@main.route('/megaminds')
@login_required
def megaminds():
    return render_template('megaminds.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)