from datetime import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    megapitch = db.relationship('Megapitch',backref = 'user',lazy="dynamic")
   
    
    
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User {self.username}'

class Megapitch(db.Model):
        __tablename__ = 'megapitch'

        id =db.Column(db.Integer,primary_key = True)
        title= db.Column(db.String(255))
        theme = db.Column(db.String(255))
        pitch = db.Column(db.String(255))
        contributors= db.Column(db.String(255))
        country =db.Column(db.String(255))
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
       
        
        

        def save_megapitch(self):
                db.session.add(self)
                db.session.commit()

        @classmethod
        def get_megapitch(cls, theme):
                megapitches = Megapitch.query.filter_by(theme=theme).all()
                return megapitches


def __repr__(self):
        return  

# class Comment(db.Model):
#         __tablename__ = 'comments'

#         id =db.Column(db.Integer,primary_key = True)
#         comment = db.Column(db.String(255))
#         user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#         megapitch_id = db.Column(db.Integer, db.ForeignKey('megapitch.id'))
#         posted = db.Column(db.DateTime,default=datetime.utcnow)
        
        

#         def save_comments(self):
#                 db.session.add(self)
#                 db.session.commit()

# def __repr__(self):
#         return  



        