from app.models.models import User
from app import db

class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def create_user(data):
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role_id=data['role_id']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
