from flask import request, current_app as app, render_template, Blueprint, redirect
# from App.domain.models.catetos import Catetos
# from App.domain.models.user import User
from App.domain.services.catetos_service import calcHipo
# from App.usecase.create_catetos import UCCreateCatetos as uc
# from App.domain.services.catetos_service import create_catetos

calc = Blueprint(name="-", import_name='cateto', url_prefix='/calcular')

@calc.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        res = calcHipo(request.form.get('catOp'), request.form.get('catAd'))
        print(res)
        print("PASSEI AQ POST")
        return render_template('calculator.html')
    else:
        return render_template('calculator.html')


@calc.route('/', methods=['GET','POST'])
def calculator():
    if request.method == 'POST':
        return result()
    return render_template('calculator.html')
