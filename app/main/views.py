from flask import render_template,redirect,url_for, abort

from app.models import User
from . import main
from flask_login import login_required
from .forms import UpdateProfile
from .. import db


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

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
