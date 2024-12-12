from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app import create_app, db
import pytest

@pytest.fixture
def app_context():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app

def test_user_service(app_context):
    from app.services.user_service import UserService

    data = {
        'username': 'serviceuser',
        'email': 'service_user@example.com',  # Asegúrate de usar un correo único
        'password': 'password',
        'role_id': 1
    }

    # Agregar un usuario
    user = UserService.add_user(data)
    assert user.username == 'serviceuser'

    # Listar los usuarios
    users = UserService.list_users()
    assert len(users) > 0
    assert any(u['email'] == 'service_user@example.com' for u in users)
