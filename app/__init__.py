from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flasgger import Swagger

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minimercado.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'super_secret_key'

    Swagger(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Importar después de inicializar 'db' para evitar importación circular
    with app.app_context():
        from app.models import models
        db.create_all()

    # Registrar blueprints
    from .controllers import routes
    app.register_blueprint(routes.bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models.models import User
    return User.query.get(int(user_id))
