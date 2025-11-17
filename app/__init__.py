from flask import Flask 
from config import Config 
from app.extensions import db,login_manager,migrate
from app.routes.auth import auth_bp
from app.routes.blog import blog_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)
    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)
    
    return app 
