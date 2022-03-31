from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
 
myapp_obj = Flask(__name__)
myapp_obj.config['SECRET_KEY'] = 'Password' 
from app import routes
