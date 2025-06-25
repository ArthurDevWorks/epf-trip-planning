from models.user import User

class AuthService:
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            return user
        return None