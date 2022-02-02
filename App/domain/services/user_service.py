from persistence.database.database_objects import create_user
from App.domain.models.user import User


def create(user=User()):
    create_user(user.email, user.name)
