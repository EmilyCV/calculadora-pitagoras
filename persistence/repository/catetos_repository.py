from App.domain.interfaces.repository import CatetosRepository
from persistence.database.database_objects import Catetos
from persistence.database.database import session

class Catetos(CatetosRepository):
    def create(catetos):
        catetos_database = Catetos(
            cateto_oposto=catetos.cateto_oposto,
            cateto_adjacente = catetos.cateto_adjacente,
            resultado = catetos.resultado,
            email = catetos.email
        )
        session.add(catetos_database)
        session.flush()
        session.refresh(catetos_database)
        session.commit()