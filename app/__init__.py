from flask import Flask,render_template
from extensions import db,login_manager
import os
from dotenv import load_dotenv
from app.routes.routes import  auth_bp,app_bp
load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.secret_key = os.getenv("SECRET_KEY")
    login_manager.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(app_bp,url_prefix="")
    return app