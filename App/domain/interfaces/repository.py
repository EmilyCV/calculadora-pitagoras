import abc
from App.domain.models.user import User
from App.domain.models.catetos import Catetos

class UserRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, user:object):
        raise NotImplementedError

    # @abc.abstractmethod
    # def get(self, reference) -> User:
    #     raise NotImplementedError

class CatetosRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, catetos:object):
        raise NotImplementedError

    # @abc.abstractmethod
    # def get(self, reference) -> Catetos:
    #     raise NotImplementedError