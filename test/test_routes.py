import pytest
from app import create_app, db
from app.models.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_holi(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hola desde Flask!" in response.data

def test_manage_users_get(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_manage_users_post(client):
    # Crear un usuario nuevo
    response = client.post('/users', json={
        'username': 'testuser',
        'email': 'unique_user@example.com',  # Asegúrate de usar un correo único
        'password': 'password',
        'role_id': 1
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User created successfully'

    # Verificar que el usuario fue creado
    response = client.get('/users')
    assert len(response.json) > 0
    assert any(user['email'] == 'unique_user@example.com' for user in response.json)
