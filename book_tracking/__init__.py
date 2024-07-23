from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import sys

# Setting system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import main, auth
        app.register_blueprint(main.main_bp)
        app.register_blueprint(auth.auth_bp)

        from .repos.alchemy import alchemy
        app.repo = alchemy()
    
    return app