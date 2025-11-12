from app.extensions import db,login_manager 
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash
from datetime import datetime
class Auth(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    username = db.Column(db.String(100),nullable=False)
    password  =  db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),nullable=True)
    

    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime,index=True,nullable=True)

    def __repr__(self):
        return f'<user {self.email}>'
    
    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
        db.session.commit()


    def restore(self):
        self.deleted_at = None 
        db.session.commit()

    @property 
    def is_deleted(self):
        return self.deleted_at is not None

@login_manager.user_loader 
def load_user(id):
     return Auth.query.get(int(id))

