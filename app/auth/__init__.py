# app/auth/__init__.py

from flask import Blueprint

autentification = Blueprint('autentification', __name__, template_folder='templates')

from app.auth import routes