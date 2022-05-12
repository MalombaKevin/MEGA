from flask import render_template,redirect,url_for, abort, request
from app.models import Megapitch, User
from . import main
from flask_login import login_required, current_user
from .forms import UpdateProfile, addMegaPitch
from .. import db
from .. import db,photos


@main.route('/')

def index():
  
    return render_template('index.html')

@main.route('/megapitch/new')
@login_required
def megaminds():
    user = User.query.filter_by(id = current_user.id).first()


    if user is None:
        abort(404)
    
    megaForm=addMegaPitch()

    if megaForm.validate_on_submit():
        theme = megaForm.theme.data
        title = megaForm.title.data
        contributors = megaForm.contributors.data
        pitch = megaForm.pitch.data

        new_mega_pitch = Megapitch(theme=theme, title=title, contributors=contributors, pitch=pitch)
    
        new_mega_pitch.save_megapitch()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/megapitch.html', megaForm = megaForm)
    
   

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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))