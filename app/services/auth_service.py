from app.models.Auth import Auth 
from app.extensions import db 
from flask_login import login_user,logout_user
from werkzeug.security import generate_password_hash,check_password_hash

def register_user(username,email,password,address):
    if Auth.query.filter_by(email=email).first():
        return None, "Email Already Exists !"
    
    hashed_password = generate_password_hash(password)
    user = Auth(email=email,username=username,address=address,password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user,None 


def authenticate_user(email,password):
    user = Auth.query.filter_by(email=email).first()
    if user and user.check_password(password):
        login_user(user)
        return True 
    return False 


def logout_current_user():
    logout_user()