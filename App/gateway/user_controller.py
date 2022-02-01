from flask import Flask, request, render_template
from App.domain.services.user import create

def create_user_controller():
    email = request.form['email']
    name = request.form['name']
    create(email, name)
