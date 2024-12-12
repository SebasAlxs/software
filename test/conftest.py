import pytest
from app import create_app, db

@pytest.fixture(scope="function")
def app_context():
    """Crea un contexto de aplicación limpio para cada prueba."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Crea las tablas en memoria
        yield app  # Entrega el contexto de aplicación a las pruebas
        db.session.rollback()  # Reversa las transacciones pendientes
        db.drop_all()  # Limpia la base de datos
