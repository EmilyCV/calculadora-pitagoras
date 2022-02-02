from flask import request
from App.domain.services.user_service import create
from App.domain.models.user import User

# def create_user_controller():
#     email = request.form['email']
#     name = request.form['name']
#     create(email, name)

# Flask(__name__).route("/create", methods=['POST'])
def create_user_controller(user=User()):
    user.email = request.form['email']
    user.name = request.form['name']
    return create(user)