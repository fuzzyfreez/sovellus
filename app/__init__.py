from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
login_manager = LoginManager()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fuzzyfreez:xinu@localhost/tsoha'

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .routes import register_routes
        register_routes(app)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
