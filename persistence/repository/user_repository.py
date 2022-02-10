from App.domain.models.user import User
from persistence.database.database_objects import Users
from App.domain.interfaces.repository import UserRepository
from persistence.database.database import session


class User(UserRepository):
    def create(user):
        user_database = Users(
            email=user.email,
            name=user.name
        )
        session.add(user_database)
        session.flush()
        session.refresh(user_database)
        session.commit()
