from App.domain.models.catetos import Catetos
from persistence.repository.catetos_repository import Catetos
# from App.usecase.create_catetos import UCCreateCatetos
from persistence.database.database_objects import create_catetos
import math

def create(catetos=Catetos()):
    print("RESULTADO")
    resultado = float(calcHipo())
    Catetos.create(catetos)  
    # create_catetos()

def calcHipo(ops, adj):
    # print(catetos.email)
    # print(user.email)

    # catOp = float(catetos.cateto_oposto)
    # catAd = float(catetos.cateto_adjacente)

    # hipotenusa = ((catOp**2)+(catAd**2))**(1/2)

    # catetos.resultado = hipotenusa
    # print("----------")
    # print(user.email)
    # print(catetos.email)
    # catetos.email = user.email
    # print(catetos.email)
    
    # return create(catetos)
    resultado = math.sqrt(
            (math.pow(ops, 2)+(math.pow(adj, 2))), (2))
    return resultado