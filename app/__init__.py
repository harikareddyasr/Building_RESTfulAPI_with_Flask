from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.utils.error_handlers import register_error_handlers
from dotenv import load_dotenv
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2 MB limit
    
    db.init_app(app)
    jwt.init_app(app)
    
    from app.routes.public_routes import public
    from app.routes.admin_routes import admin
    app.register_blueprint(public)
    app.register_blueprint(admin, url_prefix='/admin')
    
    register_error_handlers(app)
    
    return app
