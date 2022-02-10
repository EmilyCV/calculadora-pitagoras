# from persistence.database.database_objects import create_user
from App.domain.models.user import User
from persistence.repository.user_repository import User


def create(new_user=User()):
    User.create(new_user)
    # create_user(user.email, user.name)
