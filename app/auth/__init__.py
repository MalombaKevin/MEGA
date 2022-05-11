from flask import Blueprint

from ..main import forms

auth = Blueprint('auth',__name__)

from . import views

