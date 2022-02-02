from flask import request, Response
from App.domain.models.catetos import Catetos
from App.domain.models.user import User
from App.domain.services.catetos_service import create_catetos


def create_catetos_controller(catetos=Catetos(), user=User()):
    catetos.cateto_oposto = request.form['catOp']
    catetos.cateto_adjacente = request.form['catAd']

    catOp = float(catetos.cateto_oposto)
    catAd = float(catetos.cateto_adjacente)

    hipotenusa = ((catOp**2)+(catAd**2))**(1/2)

    catetos.resultado = hipotenusa
    print("----------")
    print(user.email)
    catetos.email = user.email

    return create_catetos(catetos.cateto_oposto, catetos.cateto_adjacente, catetos.resultado, catetos.email)
