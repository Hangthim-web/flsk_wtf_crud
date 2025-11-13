from app.models.Auth import Auth 
from app.extensions import db 
from flask_login import login_user,logout_user
from werkzeug.security import generate_password_hash,check_password_hash

def register_user(email,password):
    if User.query.filter_by(email=email).first():
        return None, "Email Already Exists !"
    
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return User,None 


def authenticate_user(email,password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        login_user(user)
        return True 
    return False 


def logout_current_user():
    logout_user()