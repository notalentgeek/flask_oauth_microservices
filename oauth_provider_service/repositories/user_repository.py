from connections.db_connection import db
from models.user_model import UserModel


class UserRepository:
    @staticmethod
    def find_by_username(username):
        return UserModel.query.filter_by(username=username).first()

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()
