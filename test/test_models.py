from app.models.models import User, Role
from app import db, create_app
import pytest

@pytest.fixture
def app_context():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app

def test_user_model(app_context):
    # Verificar si ya existe el rol 'Admin'
    role = Role.query.filter_by(name="Admin").first()
    if not role:
        role = Role(name="Admin")
        db.session.add(role)
        db.session.commit()

    # Crear un usuario asociado al rol
    user = User(username="testuser", email="testuser@example.com", password="password", role_id=role.id)
    db.session.add(user)
    db.session.commit()

    # Verificar que el usuario fue creado correctamente
    assert user in db.session
    assert user.role.name == "Admin"