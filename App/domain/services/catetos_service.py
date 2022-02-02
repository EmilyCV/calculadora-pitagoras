from App.domain.models.catetos import Catetos
from persistence.database.database_objects import create_catetos

def create_catetos_service(catetos=Catetos()):
    create_catetos()