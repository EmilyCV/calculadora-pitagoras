from flask import request, current_app as app, redirect, url_for, render_template, Blueprint
from App.domain.services.user_service import create as createService
from App.domain.models.user import User



user = Blueprint(name='__name__', import_name="user")

@user.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        createService(User(email = request.form.get('email'), name = request.form.get('name')))
        return render_template('calculator.html')
    return render_template('index.html')

# def create_user_controller():
#     email = request.form['email']
#     name = request.form['name']
#     create(email, name)

# Flask(__name__).route("/create", methods=['POST'])
# def create_user_controller(user=User()):
#     user.email = request.form['email']
#     user.name = request.form['name']
#     return create(user)