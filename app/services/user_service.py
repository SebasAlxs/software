from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def list_users():
        users = UserRepository.get_all_users()
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]

    @staticmethod
    def add_user(data):
        return UserRepository.create_user(data)
